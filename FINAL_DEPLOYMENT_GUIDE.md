# 🚀 Final Deployment Guide - Render

## Quick Deploy Steps

### 1. Backend (Render Web Service)

1. **Render Dashboard** → New + → Web Service
2. **Connect GitHub** → Select repository
3. **Settings:**
   - Root Directory: `backend`
   - Build: `python copy_ml_files.py && pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. **Environment Variables:**
   - `SECRET_KEY`: Generate random string
   - `ALLOWED_ORIGINS`: `https://event-review-summarizer-frontend.onrender.com` (no trailing slash)
   - `ENABLE_ML_MODEL`: Leave empty (or set to `false`) - ML model disabled by default to save memory
5. **Deploy**

### 2. Frontend (Render Static Site)

1. **Render Dashboard** → New + → Static Site
2. **Connect GitHub** → Select same repository
3. **Settings:**
   - Root Directory: `frontend`
   - Build: `npm install && npm run build`
   - Publish: `dist`
4. **Environment Variables:**
   - `VITE_API_URL`: `https://event-review-summarizer-backend.onrender.com` (no trailing slash)
5. **Deploy**

## ✅ That's It!

Your app is now live! URLs will have `#` (HashRouter):
- `https://your-frontend.onrender.com/#/register`
- `https://your-frontend.onrender.com/#/login`
- `https://your-frontend.onrender.com/#/dashboard`

## 💡 Memory Optimization

- **ML Model**: Disabled by default (saves ~200-300MB)
- **Summaries**: Use sentiment analysis (still useful!)
- **To Enable ML**: Set `ENABLE_ML_MODEL=true` and uncomment transformers/torch in requirements.txt

---

See [RENDER_DEPLOYMENT.md](./RENDER_DEPLOYMENT.md) for detailed instructions.

