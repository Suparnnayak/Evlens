# ✅ Deployment Checklist

Use this checklist to ensure everything is set up correctly.

## 📦 Pre-Deployment

- [ ] Code is committed and pushed to GitHub
- [ ] All sensitive files are in `.gitignore`
- [ ] No API keys or secrets in code
- [ ] Tested locally (backend and frontend work)

## 🚂 Backend (Railway)

### Setup
- [ ] Railway account created
- [ ] GitHub repository connected
- [ ] New service created

### Configuration
- [ ] **Root Directory**: Set to `backend` ⚠️ CRITICAL
- [ ] Build Command: Leave empty (auto-detects)
- [ ] Start Command: Leave empty (uses Procfile)

### Environment Variables
- [ ] `SECRET_KEY`: Generated/added
- [ ] `ALLOWED_ORIGINS`: Will add after frontend deployment

### Files (should exist)
- [ ] `backend/requirements.txt` ✅
- [ ] `backend/Procfile` ✅
- [ ] `backend/runtime.txt` ✅
- [ ] `backend/railway.toml` ✅

### Deployment
- [ ] Deployed successfully
- [ ] Build logs show "Python 3.12.0"
- [ ] Backend URL copied: `https://your-app.railway.app`

## ⚡ Frontend (Vercel)

### Setup
- [ ] Vercel account created
- [ ] GitHub repository connected
- [ ] Project imported

### Configuration
- [ ] **Root Directory**: Set to `frontend` ⚠️ IMPORTANT
- [ ] Framework: Vite (auto-detected)
- [ ] Build Command: `npm run build` (auto-detected)
- [ ] Output Directory: `dist` (auto-detected)

### Environment Variables
- [ ] `VITE_API_URL`: Set to Railway backend URL

### Files (should exist)
- [ ] `frontend/package.json` ✅
- [ ] `frontend/vercel.json` ✅
- [ ] `frontend/vite.config.js` ✅

### Deployment
- [ ] Deployed successfully
- [ ] Frontend URL copied: `https://your-app.vercel.app`

## 🔗 Connection

- [ ] `ALLOWED_ORIGINS` in Railway = Vercel URL
- [ ] `VITE_API_URL` in Vercel = Railway URL
- [ ] Both services redeployed after connection

## 🧪 Testing

- [ ] Frontend loads at Vercel URL
- [ ] Can register new account
- [ ] Can login
- [ ] Can upload CSV file
- [ ] Analysis results display
- [ ] No CORS errors in browser console
- [ ] No API connection errors

## ✅ Production Ready!

- [ ] Everything tested and working
- [ ] URLs saved/bookmarked
- [ ] Environment variables documented
- [ ] Team members have access (if applicable)

---

**Follow [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for detailed steps!**

