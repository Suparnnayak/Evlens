# 🚀 Complete Deployment Guide

Deploy your Event Review Summarizer to production in minutes!

## 📋 Overview

- **Frontend**: Deploy on [Vercel](https://vercel.com) (free, optimized for React)
- **Backend**: Deploy on [Railway](https://railway.app) (free tier, Python support)
- **Connection**: Frontend connects to backend via environment variables

---

## Part 1: Push to GitHub

### Step 1: Commit and Push

```bash
git add .
git commit -m "Ready for deployment: Railway + Vercel"
git push origin main
```

---

## Part 2: Deploy Backend on Railway

### Step 1: Create Railway Account

1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub
3. Click **"New Project"**

### Step 2: Connect GitHub Repository

1. **"Deploy from GitHub repo"**
2. Select your repository
3. Railway will create a new service

### Step 3: Configure Backend Service

**In Railway Dashboard → Your Service → Settings:**

1. **Root Directory**: Set to `backend` ⚠️ **CRITICAL**
2. **Build Command**: Leave empty (Railway auto-detects)
3. **Start Command**: Leave empty (uses Procfile)

**Railway will automatically:**
- Detect `requirements.txt` → Knows it's Python
- Use `runtime.txt` → Python 3.12.0
- Use `Procfile` → Start command

### Step 4: Add Environment Variables

**Variables** tab → Add:

- `SECRET_KEY`: Click "Generate" or use a random string
- `ALLOWED_ORIGINS`: Leave empty for now (add after frontend deployment)

### Step 5: Deploy

1. Railway auto-deploys on push
2. Or click **"Deploy"** → **"Redeploy"**
3. Wait for build to complete

### Step 6: Get Backend URL

1. After deployment, Railway provides a URL
2. Example: `https://your-app.railway.app`
3. **Copy this URL** - you'll need it for frontend!

---

## Part 3: Deploy Frontend on Vercel

### Step 1: Create Vercel Account

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click **"Add New Project"**

### Step 2: Import GitHub Repository

1. **"Import Git Repository"**
2. Select your repository
3. Click **"Import"**

### Step 3: Configure Frontend

**Project Settings:**

- **Framework Preset**: `Vite` (auto-detected)
- **Root Directory**: `frontend` ⚠️ **IMPORTANT**
- **Build Command**: `npm run build` (auto-detected)
- **Output Directory**: `dist` (auto-detected)
- **Install Command**: `npm install` (auto-detected)

### Step 4: Add Environment Variable

**Environment Variables** → Add:

- **Name**: `VITE_API_URL`
- **Value**: Your Railway backend URL (e.g., `https://your-app.railway.app`)
- **Environment**: Production, Preview, Development (check all)

### Step 5: Deploy

1. Click **"Deploy"**
2. Wait for build (usually 1-2 minutes)
3. Vercel provides a URL (e.g., `https://your-app.vercel.app`)

### Step 6: Get Frontend URL

1. Copy your Vercel URL
2. Example: `https://your-app.vercel.app`

---

## Part 4: Connect Frontend and Backend

### Step 1: Update Backend CORS

**In Railway Dashboard → Variables:**

1. Add/Update `ALLOWED_ORIGINS`
2. Value: Your Vercel URL (e.g., `https://your-app.vercel.app`)
3. If you have multiple, separate with commas:
   ```
   https://your-app.vercel.app,http://localhost:3000
   ```

### Step 2: Update Frontend API URL

**In Vercel Dashboard → Settings → Environment Variables:**

1. Update `VITE_API_URL` with your Railway backend URL
2. Make sure it's set for all environments

### Step 3: Redeploy Both

1. **Railway**: Click "Redeploy" (to pick up new CORS setting)
2. **Vercel**: Auto-redeploys when env vars change, or manually redeploy

---

## ✅ Verify Everything Works

1. **Visit your Vercel URL**: `https://your-app.vercel.app`
2. **Register/Login**: Should work
3. **Upload CSV**: Should connect to backend
4. **View Results**: Should display analysis

---

## 🔧 Troubleshooting

### Backend Issues

**"pip: command not found"**
- ✅ Set **Root Directory** to `backend` in Railway Settings

**"Module not found"**
- ✅ Check that `requirements.txt` is in `backend/` directory
- ✅ Verify all dependencies are listed

**CORS errors**
- ✅ Update `ALLOWED_ORIGINS` in Railway with your Vercel URL
- ✅ Check backend logs for CORS errors

### Frontend Issues

**"API connection failed"**
- ✅ Check `VITE_API_URL` is set correctly in Vercel
- ✅ Verify backend URL is accessible (visit in browser)
- ✅ Check browser console for errors

**"Build failed"**
- ✅ Check Node.js version (should be 16+)
- ✅ Verify all dependencies in `package.json`
- ✅ Check build logs in Vercel

---

## 📝 Quick Reference

### Backend (Railway)
- **Root Directory**: `backend`
- **URL**: `https://your-app.railway.app`
- **Environment Variables**: `SECRET_KEY`, `ALLOWED_ORIGINS`

### Frontend (Vercel)
- **Root Directory**: `frontend`
- **URL**: `https://your-app.vercel.app`
- **Environment Variable**: `VITE_API_URL` (your Railway URL)

---

## 🎯 Deployment Checklist

### Backend (Railway)
- [ ] Account created
- [ ] Repository connected
- [ ] Root Directory set to `backend`
- [ ] Environment variables added (`SECRET_KEY`, `ALLOWED_ORIGINS`)
- [ ] Deployed successfully
- [ ] Backend URL copied

### Frontend (Vercel)
- [ ] Account created
- [ ] Repository connected
- [ ] Root Directory set to `frontend`
- [ ] Environment variable added (`VITE_API_URL`)
- [ ] Deployed successfully
- [ ] Frontend URL copied

### Connection
- [ ] `ALLOWED_ORIGINS` updated with Vercel URL
- [ ] `VITE_API_URL` updated with Railway URL
- [ ] Both services redeployed
- [ ] Tested end-to-end

---

## 🎉 You're Live!

Your application is now deployed and accessible to the world!

- **Frontend**: `https://your-app.vercel.app`
- **Backend API**: `https://your-app.railway.app`
- **API Docs**: `https://your-app.railway.app/docs`

---

## 📚 Additional Resources

- [Railway Documentation](https://docs.railway.app)
- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)

---

**Need help?** Check the build logs in Railway/Vercel dashboards for detailed error messages.

