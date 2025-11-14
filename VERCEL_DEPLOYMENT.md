# Deploying Both Frontend & Backend on Vercel

## ⚠️ Important Limitations

**Your backend uses heavy ML dependencies:**
- `torch` (~2GB)
- `transformers` (~500MB)
- ML models downloaded at runtime

**Vercel Limitations:**
- Serverless function size limit: **50MB** (uncompressed)
- Execution timeout: **10 seconds** (Hobby), **60 seconds** (Pro)
- Cold starts can be **very slow** with ML models

## 🎯 Two Options

### Option 1: Lightweight Backend (Recommended for Vercel)

Remove heavy ML dependencies and use lighter alternatives:

**Pros:**
- ✅ Works within Vercel limits
- ✅ Faster cold starts
- ✅ Single deployment

**Cons:**
- ❌ Less powerful ML models
- ❌ May need to simplify analysis

### Option 2: Hybrid Approach (Best Performance)

- **Frontend**: Vercel
- **Backend API (Auth/File Upload)**: Vercel serverless functions
- **ML Processing**: External service (Hugging Face Inference API, or separate Railway deployment)

---

## 🚀 Option 1: Full Vercel Deployment (Lightweight)

### Step 1: Create Vercel API Routes

Create `api/` directory in your project root:

```
project-root/
├── api/
│   ├── auth/
│   │   ├── login.py
│   │   ├── register.py
│   │   └── me.py
│   ├── analyze.py
│   └── __init__.py
├── frontend/
└── ...
```

### Step 2: Update Dependencies

Create `api/requirements.txt` with lightweight alternatives:

```txt
fastapi==0.104.1
python-multipart==0.0.6
sqlalchemy==2.0.23
pydantic[email]==2.5.0
python-jose[cryptography]==3.3.0
bcrypt==4.0.1
python-dateutil==2.8.2
pandas==2.1.3
numpy==1.26.2
scikit-learn==1.3.2
textblob==0.17.1
# Remove: torch, transformers (too large)
# Use: Hugging Face Inference API instead
requests==2.32.5
```

### Step 3: Use External ML API

Instead of loading models locally, use Hugging Face Inference API:

```python
# api/ml_service.py
import requests
import os

HUGGINGFACE_API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def generate_summary(text: str) -> str:
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}
    response = requests.post(
        HUGGINGFACE_API_URL,
        headers=headers,
        json={"inputs": f"Summarize: {text}"}
    )
    return response.json()[0]["summary_text"]
```

---

## 🚀 Option 2: Hybrid Vercel Deployment (Recommended)

### Architecture:
- **Frontend**: Vercel (React app)
- **Backend API**: Vercel serverless functions (auth, file handling)
- **ML Processing**: Railway/Render (heavy ML work)

This gives you:
- ✅ Fast frontend on Vercel
- ✅ Simple API routes on Vercel
- ✅ Heavy ML processing on dedicated server
- ✅ Best of both worlds

---

## 📝 Quick Setup for Option 2 (Hybrid)

### 1. Deploy Frontend on Vercel
- Standard Vite deployment
- Set `VITE_API_URL` to your backend

### 2. Create Lightweight API Routes on Vercel

Create `api/` folder in project root:

```python
# api/auth/login.py
from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Forward to your Railway backend
        import requests
        railway_url = os.getenv("RAILWAY_BACKEND_URL")
        # Proxy request to Railway
        # ...
```

### 3. Deploy ML Backend on Railway
- Keep your full FastAPI backend with ML models
- Use it only for `/api/analyze` endpoint

---

## 🎯 My Recommendation

**Use Option 2 (Hybrid):**
1. Deploy frontend on Vercel ✅
2. Deploy full backend on Railway ✅
3. Use Vercel rewrites to proxy API calls

This is the **best balance** of:
- Performance
- Cost (both free tiers)
- Ease of deployment
- No limitations

---

## 📋 Next Steps

If you want to proceed with **full Vercel deployment**, I can:
1. Create lightweight API routes
2. Set up Hugging Face Inference API integration
3. Update dependencies

If you want the **hybrid approach** (recommended), follow the original deployment guide.

**Which option would you prefer?**

