# Project Summary - Event Review Summarizer

## Overview
This project is a full-stack application for analyzing event reviews from CSV files and generating AI-powered summaries with sentiment analysis. It has been upgraded from a prototype Streamlit app to a production-ready application with authentication, modern UI, and improved ML pipeline.

## What Was Built

### 1. Backend (FastAPI)
- **Authentication System**: JWT-based authentication with user registration and login
- **Database**: SQLite database with SQLAlchemy ORM (can be upgraded to PostgreSQL)
- **API Endpoints**:
  - `POST /api/auth/register` - Register new user
  - `POST /api/auth/login` - Login and get access token
  - `GET /api/auth/me` - Get current user info
  - `POST /api/analyze` - Upload CSV and generate summary (requires authentication)
- **ML Service**: Improved ML pipeline with lazy loading and better error handling
- **File Upload**: Secure file upload with automatic cleanup

### 2. Frontend (React)
- **Authentication Pages**: 
  - Login page with email/password
  - Registration page with username, email, and password
- **Dashboard**:
  - CSV file upload interface
  - Results display with summary and sentiment analysis
  - Visualizations (pie charts, bar charts)
  - Download results as JSON
- **UI/UX**: 
  - Modern, responsive design with Tailwind CSS
  - Loading states and error handling
  - User-friendly interface

### 3. ML Improvements
- **All Reviews Processing**: Now processes ALL reviews, not just samples
- **Lazy Model Loading**: Models loaded only when needed
- **Improved Sentiment Analysis**: More nuanced sentiment classification
- **Better Text Processing**: Smart text chunking and truncation
- **Key Insights Extraction**: Automatic extraction of key insights
- **Error Handling**: Comprehensive error handling and logging

## Project Structure

```
.
├── backend/              # FastAPI backend
│   ├── main.py          # API entry point
│   ├── auth.py          # Authentication utilities
│   ├── database.py      # Database configuration
│   ├── models.py        # Database models
│   ├── schemas.py       # Pydantic schemas
│   ├── ml_service.py    # ML pipeline service
│   └── requirements.txt # Backend dependencies
├── frontend/            # React frontend
│   ├── src/
│   │   ├── pages/       # Page components
│   │   ├── components/  # Reusable components
│   │   └── contexts/    # React contexts
│   └── package.json     # Frontend dependencies
├── src/                 # Original ML code
│   ├── analyzer.py      # CSV analysis
│   └── summarizer.py    # Summary generation
├── README.md            # Main documentation
├── SETUP.md             # Setup instructions
├── QUICK_START.md       # Quick start guide
├── ML_IMPROVEMENTS.md   # ML improvements documentation
└── requirements.txt     # Main dependencies
```

## Key Features

### Authentication
- User registration with email, username, and password
- JWT-based authentication
- Protected routes
- Session management

### CSV Analysis
- Upload CSV files with event reviews
- Automatic analysis of reviews
- AI-powered summary generation
- Sentiment analysis with visualizations
- Key insights extraction
- Download results as JSON

### UI/UX
- Modern, responsive design
- Loading states
- Error handling
- Visual feedback
- User-friendly interface

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **JWT** - Authentication tokens
- **Transformers** - AI model for summarization
- **TextBlob** - Sentiment analysis
- **Pandas** - CSV processing

### Frontend
- **React** - UI library
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Recharts** - Data visualization
- **Axios** - HTTP client
- **React Router** - Navigation

## Setup Instructions

### Backend
1. Navigate to `backend/` directory
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run server: `python main.py`

### Frontend
1. Navigate to `frontend/` directory
2. Install dependencies: `npm install`
3. Start dev server: `npm run dev`

## Usage

1. **Register/Login**: Create an account or login
2. **Upload CSV**: Upload a CSV file with event reviews
3. **Analyze**: Click "Analyze Reviews" to process the file
4. **View Results**: See the generated summary, sentiment analysis, and insights
5. **Download**: Download the results as JSON

## CSV Format

```csv
event_name,review_text
TechFest 2025,"Great event with amazing speakers!"
MusicFest 2025,"The sound quality could be better."
```

## ML Improvements

1. **All Reviews Processing**: Processes all reviews, not just samples
2. **Lazy Model Loading**: Models loaded only when needed
3. **Improved Sentiment Analysis**: More nuanced sentiment classification
4. **Better Text Processing**: Smart text chunking and truncation
5. **Key Insights Extraction**: Automatic extraction of key insights
6. **Error Handling**: Comprehensive error handling and logging

## Future Improvements

- [ ] Better sentiment models (transformer-based)
- [ ] Topic modeling
- [ ] User dashboard with history
- [ ] Support for multiple file formats
- [ ] Email notifications
- [ ] Rate limiting
- [ ] Caching for better performance
- [ ] Support for larger CSV files
- [ ] Real-time processing progress
- [ ] Export to PDF format

## Documentation

- **README.md** - Main documentation
- **SETUP.md** - Detailed setup instructions
- **QUICK_START.md** - Quick start guide
- **ML_IMPROVEMENTS.md** - ML improvements documentation

## License

MIT License

## Contributors

Team EVLENS

