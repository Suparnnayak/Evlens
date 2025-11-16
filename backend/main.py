"""
FastAPI Backend for Event Review Summarizer
"""
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional
import uvicorn
import os
import shutil
from datetime import datetime, timedelta
from jose import JWTError, jwt

from database import SessionLocal, engine, Base
from models import User
from schemas import UserCreate, UserResponse, Token, AnalysisResponse
from auth import get_current_user, get_password_hash, verify_password, create_access_token
from ml_service import analyze_csv_file, generate_summary_improved
import logging

logger = logging.getLogger(__name__)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Event Review Summarizer API",
    description="API for generating event summaries from CSV reviews",
    version="1.0.0"
)

# CORS middleware
# Get allowed origins from environment variable or use defaults
allowed_origins_str = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173,https://event-review-summarizer-frontend.onrender.com"
)

# Split by comma and strip whitespace and trailing slashes
allowed_origins = [
    origin.strip().rstrip('/') for origin in allowed_origins_str.split(",") if origin.strip()
]

# Always include the frontend URL as a fallback (even if env var is missing)
frontend_url = "https://event-review-summarizer-frontend.onrender.com"
if frontend_url not in allowed_origins:
    allowed_origins.append(frontend_url)

# Log CORS configuration for debugging
print(f"CORS Allowed Origins: {allowed_origins}")
print(f"ALLOWED_ORIGINS env var: {allowed_origins_str}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"],
    allow_headers=["*"],
    expose_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/auth/login")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Event Review Summarizer API", "status": "running"}

@app.options("/{full_path:path}")
async def options_handler(full_path: str):
    """Handle OPTIONS requests for CORS preflight"""
    return {"message": "OK"}


@app.post("/api/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Register a new user"""
    # Check if user already exists
    db_user = db.query(User).filter(User.email == user_data.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    # Create new user
    hashed_password = get_password_hash(user_data.password)
    db_user = User(
        email=user_data.email,
        username=user_data.username,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return UserResponse(
        id=db_user.id,
        email=db_user.email,
        username=db_user.username,
        created_at=db_user.created_at
    )


@app.post("/api/auth/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login and get access token"""
    user = db.query(User).filter(User.email == form_data.username).first()
    
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/api/auth/me", response_model=UserResponse)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    """Get current user information"""
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        username=current_user.username,
        created_at=current_user.created_at
    )


@app.post("/api/analyze", response_model=AnalysisResponse)
async def analyze_csv(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """Upload CSV file and generate event summary"""
    import asyncio
    from concurrent.futures import ThreadPoolExecutor
    
    if not file.filename.endswith('.csv'):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must be a CSV file"
        )
    
    # Create uploads directory if it doesn't exist
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    
    # Save uploaded file
    file_path = os.path.join(upload_dir, f"{current_user.id}_{datetime.now().timestamp()}.csv")
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Run analysis in thread pool to avoid blocking
        # This prevents timeout issues with long-running ML operations
        loop = asyncio.get_event_loop()
        executor = ThreadPoolExecutor(max_workers=1)
        
        # Run analysis with timeout (5 minutes)
        try:
            report = await asyncio.wait_for(
                loop.run_in_executor(executor, analyze_csv_file, file_path),
                timeout=300.0  # 5 minutes timeout
            )
            summary = await asyncio.wait_for(
                loop.run_in_executor(executor, generate_summary_improved, report),
                timeout=120.0  # 2 minutes timeout for summary
            )
        except asyncio.TimeoutError:
            # Clean up file on timeout
            if os.path.exists(file_path):
                os.remove(file_path)
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Analysis took too long. Please try with a smaller CSV file or try again later."
            )
        finally:
            executor.shutdown(wait=False)
        
        # Clean up file
        if os.path.exists(file_path):
            os.remove(file_path)
        
        return AnalysisResponse(
            report=report,
            summary=summary,
            message="Analysis completed successfully"
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        # Clean up file on error
        if os.path.exists(file_path):
            os.remove(file_path)
        logger.error(f"Error processing file: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error processing file: {str(e)}"
        )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

