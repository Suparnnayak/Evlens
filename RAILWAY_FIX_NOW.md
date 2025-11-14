# 🚨 Railway Fix: pip: command not found

## The Problem
Railway can't find `pip` because it's not detecting Python properly.

## ✅ THE FIX (Do This Now)

### Step 1: Set Root Directory (CRITICAL!)

1. **Railway Dashboard** → Your Service
2. Click **"Settings"** tab
3. Scroll to **"Service Settings"**
4. Find **"Root Directory"** field
5. **Set it to**: `backend` (exactly this, no slashes, no quotes)
6. Click **"Save"**

**This is the #1 cause of the error!**

### Step 2: Clear Build Settings (Let Railway Auto-Detect)

In the same Settings page:

- **Build Command**: Leave **EMPTY** (Railway will auto-detect from requirements.txt)
- **Start Command**: Leave **EMPTY** (Railway will use Procfile)

OR manually set:
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Add Environment Variables

**Variables** tab:
- `SECRET_KEY`: Generate a random string
- `ALLOWED_ORIGINS`: Your frontend URL (add later)

### Step 4: Redeploy

1. Click **"Deploy"** → **"Redeploy"**
2. Or push to GitHub (auto-deploy)

## 🔍 What Should Happen

After setting Root Directory to `backend`, Railway should:
1. Detect `backend/requirements.txt` → Knows it's Python
2. Detect `backend/runtime.txt` → Uses Python 3.12.0
3. Run `pip install -r requirements.txt` automatically
4. Use `backend/Procfile` for start command

## ✅ Verify in Build Logs

You should see:
```
Detected Python project
Python 3.12.0
Installing dependencies...
pip install -r requirements.txt ✅
```

## 🎯 Quick Checklist

- [ ] Root Directory set to `backend` in Railway Settings
- [ ] Build Command is EMPTY (or `pip install -r requirements.txt`)
- [ ] Start Command is EMPTY (or `uvicorn main:app --host 0.0.0.0 --port $PORT`)
- [ ] `backend/requirements.txt` exists
- [ ] `backend/Procfile` exists
- [ ] `backend/runtime.txt` exists (Python 3.12.0)

## 🆘 Still Not Working?

1. **Double-check Root Directory**: Must be exactly `backend` (case-sensitive)
2. **Check file locations**: All files should be in `backend/` directory
3. **Try manual build**: Set Build Command to `pip install -r requirements.txt`
4. **Check Railway logs**: Look for "Detected" messages

## 💡 Alternative: Use Railway CLI

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Link project
railway link

# Set root directory
railway variables set RAILWAY_ROOT_DIRECTORY=backend

# Deploy
railway up
```

---

**The Root Directory MUST be set to `backend` in Railway Settings!** 🎯

This is 99% of the time the issue.

