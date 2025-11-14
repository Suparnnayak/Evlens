# 🚨 Railway Quick Fix - pip: command not found

## The Problem
Railway isn't detecting Python, so `pip` isn't available during build.

## ✅ THE FIX

### Step 1: Set Root Directory in Railway

**CRITICAL**: Railway must know the root directory is `backend`

1. Railway Dashboard → Your Service
2. **Settings** tab
3. **Service Settings** section
4. **Root Directory**: Set to `backend` (exactly this, no slash)
5. **Save**

### Step 2: Verify Build Settings

In Railway Settings, make sure:

- **Root Directory**: `backend` ✅
- **Build Command**: Leave empty (Railway will auto-detect)
- **Start Command**: Leave empty OR set to: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Railway Should Auto-Detect

Railway should automatically:
- Detect `requirements.txt` → Knows it's Python
- Detect Python version from `runtime.txt` or `.python-version`
- Install dependencies with pip
- Use `Procfile` for start command

### Step 4: Clear and Redeploy

1. Railway Dashboard → Your Service
2. Click **"Deploy"** → **"Clear build cache"** (if available)
3. Click **"Redeploy"**

## 🔍 Verify

After redeploy, check build logs. You should see:
```
Detected Python project
Installing dependencies...
pip install -r requirements.txt
```

## 📋 Files That Help Railway Detect Python

✅ `backend/requirements.txt` - Tells Railway it's Python
✅ `backend/runtime.txt` - Specifies Python 3.12.0
✅ `backend/.python-version` - Alternative Python version spec
✅ `backend/Procfile` - Start command
✅ `backend/railway.toml` - Railway config

## 🎯 Most Important

**Set Root Directory to `backend` in Railway Settings!**

This is the #1 cause of this error. Railway needs to know where your Python code is.

## 🆘 Still Not Working?

1. **Check Root Directory**: Must be exactly `backend` (not `/backend` or `./backend`)
2. **Verify requirements.txt exists**: Should be in `backend/requirements.txt`
3. **Check build logs**: Look for "Detected Python" message
4. **Try manual build command**: Set to `pip install -r requirements.txt` in settings

---

**The Root Directory setting is critical! Make sure it's set to `backend`.** 🎯

