# 🔗 How to Connect Frontend (Vercel) and Backend (Railway)

## Quick Connection Steps

### Step 1: Deploy Backend First (Railway)

1. Deploy backend on Railway
2. Get your Railway URL: `https://your-app.railway.app`
3. **Copy this URL** ✅

### Step 2: Deploy Frontend (Vercel)

1. Deploy frontend on Vercel
2. **Before deploying**, add environment variable:
   - **Name**: `VITE_API_URL`
   - **Value**: Your Railway URL (e.g., `https://your-app.railway.app`)
3. Deploy
4. Get your Vercel URL: `https://your-app.vercel.app`
5. **Copy this URL** ✅

### Step 3: Connect Them

**In Railway Dashboard → Variables:**
- Add/Update `ALLOWED_ORIGINS`
- Value: Your Vercel URL (e.g., `https://your-app.vercel.app`)

**In Vercel Dashboard → Environment Variables:**
- Verify `VITE_API_URL` is set to your Railway URL

### Step 4: Redeploy

1. **Railway**: Redeploy to pick up new CORS setting
2. **Vercel**: Should auto-redeploy, or manually redeploy

---

## ✅ That's It!

Your frontend and backend are now connected!

- Frontend calls: `VITE_API_URL/api/*` → Goes to Railway backend
- Backend allows: Requests from `ALLOWED_ORIGINS` → Your Vercel URL

---

## 🔍 Test the Connection

1. Visit your Vercel URL
2. Try to register/login
3. If it works → Connection successful! ✅
4. If errors → Check browser console and backend logs

---

## 📝 Environment Variables Summary

### Railway (Backend)
```
SECRET_KEY=your-secret-key
ALLOWED_ORIGINS=https://your-app.vercel.app
```

### Vercel (Frontend)
```
VITE_API_URL=https://your-app.railway.app
```

---

**The key is: Frontend URL in Railway's ALLOWED_ORIGINS, and Backend URL in Vercel's VITE_API_URL!** 🎯

