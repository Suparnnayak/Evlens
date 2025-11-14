# Quick Deployment Guide 🚀

## TL;DR - Deploy in 3 Steps

### 1️⃣ Push to GitHub

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 2️⃣ Deploy Backend (Railway - Recommended)

1. Go to [railway.app](https://railway.app) → Sign up
2. **New Project** → **Deploy from GitHub repo**
3. Select your repo
4. **Settings**:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. **Variables** tab → Add:
   - `SECRET_KEY`: (generate a random string)
   - `ALLOWED_ORIGINS`: (add your Vercel URL later)
6. Copy the **Railway URL** (e.g., `https://your-app.railway.app`)

### 3️⃣ Deploy Frontend (Vercel)

1. Go to [vercel.com](https://vercel.com) → Sign up
2. **Add New Project** → Import your GitHub repo
3. **Configure**:
   - Framework: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
4. **Environment Variables**:
   - `VITE_API_URL`: Your Railway backend URL
5. **Deploy** → Copy your Vercel URL
6. Go back to Railway → Update `ALLOWED_ORIGINS` with your Vercel URL

## ✅ Done!

Your app is live! 🎉

- Frontend: `https://your-app.vercel.app`
- Backend: `https://your-app.railway.app`

---

## 🔧 Important Notes

1. **Backend and Frontend MUST be deployed separately** - Vercel doesn't support Python backends well
2. **Update CORS** in backend after getting frontend URL
3. **Environment variables** are crucial - don't forget them!

For detailed instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)

