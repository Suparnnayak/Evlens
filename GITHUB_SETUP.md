# GitHub Setup Guide

## Step 1: Initialize Git Repository

```bash
# In your project root (D:\Insightsummarizer)
git init
git add .
git commit -m "Initial commit: Event Review Summarizer with modern UI"
```

## Step 2: Create GitHub Repository

1. Go to [github.com](https://github.com) and sign in
2. Click the **+** icon → **New repository**
3. Repository name: `event-review-summarizer` (or any name)
4. Description: "AI-powered event review analyzer with sentiment analysis"
5. Choose **Public** or **Private**
6. **DO NOT** check "Initialize with README" (we already have files)
7. Click **Create repository**

## Step 3: Connect and Push

```bash
# Replace YOUR_USERNAME and REPO_NAME with your actual values
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

## Step 4: Verify

Go to your GitHub repository page - you should see all your files!

---

## 🔄 Future Updates

When you make changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## 📝 What Gets Pushed

✅ **Included:**
- All source code
- Configuration files
- Documentation

❌ **Excluded** (via .gitignore):
- `node_modules/`
- `venv/`
- `.env` files
- Database files (`.db`)
- Uploaded files
- Build artifacts (`dist/`)

---

## 🎯 Next Steps

After pushing to GitHub:
1. Deploy backend (see [DEPLOYMENT.md](./DEPLOYMENT.md))
2. Deploy frontend (see [DEPLOYMENT.md](./DEPLOYMENT.md))

