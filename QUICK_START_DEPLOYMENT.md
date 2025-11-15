# ⚡ Quick Start: Deploy in 5 Minutes

## 🎯 TL;DR

1. **Backend (Railway)**: Set Root Directory = `backend`, deploy
2. **Frontend (Vercel)**: Set Root Directory = `frontend`, add `VITE_API_URL`, deploy
3. **Connect**: Add Vercel URL to Railway's `ALLOWED_ORIGINS`

---

## Step-by-Step

### 1️⃣ Backend on Railway (2 min)

```
1. Go to railway.app → New Project → Deploy from GitHub
2. Select your repo
3. Settings → Root Directory: backend
4. Variables → Add SECRET_KEY (generate random string)
5. Deploy → Copy URL
```

### 2️⃣ Frontend on Vercel (2 min)

```
1. Go to vercel.com → Add New Project → Import GitHub repo
2. Settings → Root Directory: frontend
3. Environment Variables → Add:
   - Name: VITE_API_URL
   - Value: [Your Railway URL]
4. Deploy → Copy URL
```

### 3️⃣ Connect (1 min)

```
1. Railway → Variables → Add:
   - Name: ALLOWED_ORIGINS
   - Value: [Your Vercel URL]
2. Redeploy both services
```

---

## ✅ Done!

Visit your Vercel URL and test it!

**Need details?** See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

