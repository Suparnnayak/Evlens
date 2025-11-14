# Deployment Guide

This guide will help you deploy the Event Review Summarizer application to production.

## 📋 Overview

**Important**: Backend and Frontend must be deployed **separately** because:
- **Frontend**: React/Vite app → Deploy on **Vercel** (optimized for frontend)
- **Backend**: FastAPI Python app → Deploy on **Railway/Render/Fly.io** (supports Python)

## 🚀 Step-by-Step Deployment

### Part 1: Push to GitHub

#### 1. Initialize Git Repository

```bash
# In your project root directory
git init
git add .
git commit -m "Initial commit: Event Review Summarizer"
```

#### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it: `event-review-summarizer` (or any name you prefer)
3. **Don't** initialize with README, .gitignore, or license (we already have these)

#### 3. Push to GitHub

```bash
# Replace YOUR_USERNAME and REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

### Part 2: Deploy Backend (FastAPI)

#### Option A: Railway (Recommended - Easy & Free)

1. **Sign up** at [Railway.app](https://railway.app)
2. **Create New Project** → "Deploy from GitHub repo"
3. **Select your repository**
4. **Configure**:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Add Environment Variables** (if needed):
   - `SECRET_KEY`: Generate a secure random string
   - `DATABASE_URL`: Railway provides this automatically
6. **Deploy** - Railway will automatically deploy
7. **Copy the URL** (e.g., `https://your-app.railway.app`)

#### Option B: Render

1. **Sign up** at [Render.com](https://render.com)
2. **New** → "Web Service"
3. **Connect GitHub** repository
4. **Configure**:
   - Name: `event-review-summarizer-backend`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Root Directory: `backend`
5. **Add Environment Variables**:
   - `SECRET_KEY`: Your secret key
6. **Deploy**

#### Option C: Fly.io

1. **Install Fly CLI**: `curl -L https://fly.io/install.sh | sh`
2. **Sign up** at [Fly.io](https://fly.io)
3. **In backend directory**:
   ```bash
   cd backend
   fly launch
   ```
4. Follow the prompts
5. **Create `fly.toml`** (see below)

---

### Part 3: Deploy Frontend (Vercel)

#### 1. Update Frontend Configuration

**Update `frontend/vite.config.js`** to use your backend URL:

```javascript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: process.env.VITE_API_URL || 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
```

**Update `frontend/src/contexts/AuthContext.jsx`** to use environment variable:

```javascript
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'
```

#### 2. Deploy to Vercel

**Option A: Via Vercel Dashboard (Easiest)**

1. **Sign up** at [Vercel.com](https://vercel.com)
2. **Import Project** → Select your GitHub repository
3. **Configure**:
   - Framework Preset: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`
4. **Add Environment Variable**:
   - `VITE_API_URL`: Your backend URL (e.g., `https://your-app.railway.app`)
5. **Deploy**

**Option B: Via Vercel CLI**

```bash
# Install Vercel CLI
npm i -g vercel

# In frontend directory
cd frontend
vercel

# Follow prompts
# When asked for environment variables, add:
# VITE_API_URL=https://your-backend-url.railway.app
```

#### 3. Update Vercel Configuration

After deployment, update `frontend/vercel.json` with your actual backend URL:

```json
{
  "rewrites": [
    {
      "source": "/api/(.*)",
      "destination": "https://YOUR_BACKEND_URL/api/$1"
    }
  ]
}
```

---

## 🔧 Configuration Files

### Backend: `backend/fly.toml` (for Fly.io)

```toml
app = "event-review-summarizer-backend"
primary_region = "iad"

[build]
  builder = "paketobuildpacks/builder:base"

[env]
  PORT = "8000"
  PYTHON_VERSION = "3.12"

[[services]]
  http_checks = []
  internal_port = 8000
  processes = ["app"]
  protocol = "tcp"
  script_checks = []

  [services.concurrency]
    hard_limit = 25
    soft_limit = 20
    type = "connections"

  [[services.ports]]
    force_https = true
    handlers = ["http"]
    port = 80

  [[services.ports]]
    handlers = ["tls", "http"]
    port = 443

  [[services.tcp_checks]]
    grace_period = "1s"
    interval = "15s"
    restart_limit = 0
    timeout = "2s"
```

### Backend: `backend/Procfile` (for Heroku/Render)

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

### Backend: `backend/runtime.txt` (if needed)

```
python-3.12.0
```

---

## 🌐 Environment Variables

### Backend Environment Variables

Create these in your backend hosting platform:

```env
SECRET_KEY=your-super-secret-key-change-this-in-production
DATABASE_URL=sqlite:///./event_summarizer.db
# Or for PostgreSQL:
# DATABASE_URL=postgresql://user:password@host:port/dbname
```

### Frontend Environment Variables

Create in Vercel dashboard:

```env
VITE_API_URL=https://your-backend-url.railway.app
```

---

## 🔄 Updating CORS in Backend

Update `backend/main.py` to allow your frontend domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://your-frontend.vercel.app",  # Add your Vercel URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📝 Quick Deployment Checklist

### Backend Deployment
- [ ] Push code to GitHub
- [ ] Create account on Railway/Render/Fly.io
- [ ] Connect GitHub repository
- [ ] Set root directory to `backend`
- [ ] Add environment variables
- [ ] Deploy and get backend URL
- [ ] Update CORS settings with frontend URL

### Frontend Deployment
- [ ] Update `vite.config.js` with backend URL
- [ ] Update `AuthContext.jsx` to use environment variable
- [ ] Create Vercel account
- [ ] Import GitHub repository
- [ ] Set root directory to `frontend`
- [ ] Add `VITE_API_URL` environment variable
- [ ] Deploy
- [ ] Update `vercel.json` with backend URL

---

## 🐛 Troubleshooting

### Backend Issues

**Issue**: Module not found errors
- **Solution**: Make sure `requirements.txt` includes all dependencies
- Check that `ML/src` directory is accessible

**Issue**: CORS errors
- **Solution**: Update CORS origins in `backend/main.py` to include your frontend URL

**Issue**: Database errors
- **Solution**: For production, use PostgreSQL instead of SQLite
- Update `DATABASE_URL` environment variable

### Frontend Issues

**Issue**: API calls failing
- **Solution**: Check `VITE_API_URL` environment variable is set correctly
- Verify backend URL is accessible
- Check browser console for CORS errors

**Issue**: Build fails
- **Solution**: Make sure all dependencies are in `package.json`
- Check Node.js version (should be 16+)

---

## 🎯 Recommended Setup

**Best Practice**:
- **Frontend**: Vercel (free tier, excellent for React)
- **Backend**: Railway (free tier, easy Python deployment)
- **Database**: Railway PostgreSQL (or keep SQLite for small projects)

---

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [Render Documentation](https://render.com/docs)
- [Fly.io Documentation](https://fly.io/docs)

---

## 💡 Tips

1. **Always test locally** before deploying
2. **Use environment variables** for all sensitive data
3. **Monitor your deployments** for errors
4. **Set up custom domains** for production
5. **Enable HTTPS** (most platforms do this automatically)
6. **Keep your dependencies updated**

---

Good luck with your deployment! 🚀

