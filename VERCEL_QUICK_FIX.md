# Vercel Deployment - Quick Fix Guide

## Problem
Vercel deployment failing with environment variable error.

## Solution

### Step 1: Configure Root Directory

In Vercel import page:

1. Scroll to **"Root Directory"**
2. Click **"Edit"**
3. Change from `./` to **`frontend`**
4. Click outside to save

### Step 2: Add Environment Variable

1. Click dropdown arrow next to **"Environment Variables"**
2. Click **"Add New Variable"**
3. Fill in:
   ```
   Name: VITE_API_URL
   Value: http://localhost:8001/api/v1
   ```
4. Click **"Add"**

### Step 3: Verify Build Settings

Make sure these are set:
- **Framework Preset:** Vite (or Other)
- **Build Command:** `npm run build`
- **Output Directory:** `dist`
- **Install Command:** `npm install`

### Step 4: Deploy

Click **"Deploy"** button

---

## ✅ Expected Result

After 2-3 minutes:
- [ ] Build succeeds
- [ ] You get a Vercel URL: `https://your-project.vercel.app`
- [ ] Frontend loads (might show "Failed to fetch" - that's OK for now)
- [ ] Save this URL for next step

---

## ⚠️ If Still Getting Error

**Delete and retry:**

1. Delete this deployment attempt
2. Click "Back to Import"
3. Follow steps 1-4 above again
4. Deploy

Or try changing project name to something unique like: `jats-app-akash`

---

## 📝 After Frontend is Deployed

1. **Copy your Vercel URL** (e.g., `https://jats-app.vercel.app`)
2. Go to **Render** and deploy backend
3. Get Render backend URL
4. Come back to Vercel → Settings → Environment Variables
5. Update `VITE_API_URL` to: `https://your-backend-xxxx.onrender.com/api/v1`
6. Redeploy

Then both will work! ✅

---

## 🆘 Common Issues

| Error | Fix |
|-------|-----|
| "VITE_API_URL not found" | Add environment variable (Step 2) |
| "Module not found" | Set Root Directory to `frontend` (Step 1) |
| "Failed to fetch" | Normal - backend not deployed yet |
| Build timeout | Increase timeout in Vercel settings |

---

## 🎯 Checklist

- [ ] Root Directory set to `frontend/`
- [ ] VITE_API_URL environment variable added
- [ ] Build Command: `npm run build`
- [ ] Output Directory: `dist`
- [ ] Click Deploy
- [ ] Wait for success message
- [ ] Copy Vercel URL

**These steps should work!** Try again and let me know if you get a different error. 💬
