# 🚀 Backend Deployment on Render - STEP BY STEP

## ✅ Your Database Details

```
DATABASE_URL: postgresql://jats_user:H0wGLKads9NtkTMeIMcLS2EZFaUyod2p@dpg-d77ngeogjchc73d20q70-a.singapore-postgres.render.com/jats_db
Region: Singapore
Status: Active ✅
```

---

## 🎯 DEPLOY BACKEND NOW (15 minutes)

### STEP 1: Go to Render Dashboard

1. Open: https://render.com/dashboard
2. Click **"New +"** (top right)
3. Select **"Web Service"**

---

### STEP 2: Connect GitHub Repository

1. Click **"Build and deploy from a Git repository"**
2. Click **"Connect Account"** (if you haven't already)
3. Find and select: `Job_application_tracking-_system`
4. Click **"Connect"**

---

### STEP 3: Configure Basic Settings

Fill in these fields:

| Field | Value |
|-------|-------|
| **Name** | `jats-backend` |
| **Region** | `Singapore` ⭐ (same as your database!) |
| **Branch** | `main` |
| **Root Directory** | `backend` |

---

### STEP 4: Configure Build & Deploy

Find these fields:

| Field | Value |
|-------|-------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `cd backend && uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT` |

---

### STEP 5: Add Environment Variables (⭐ CRITICAL)

1. Scroll down to **"Advanced"**
2. Look for **"Environment Variables"** section
3. Click **"Add Environment Variable"** for each one:

**Add these variables one by one:**

```
DATABASE_URL = postgresql://jats_user:H0wGLKads9NtkTMeIMcLS2EZFaUyod2p@dpg-d77ngeogjchc73d20q70-a.singapore-postgres.render.com/jats_db
```

```
PYTHONPATH = /opt/render/project/src/backend:/opt/render/project/src/backend/django_app
```

```
DJANGO_SETTINGS_MODULE = config.settings
```

```
JWT_SECRET_KEY = my_super_secret_jwt_key_12345
```

```
DJANGO_SECRET_KEY = my_django_secret_key_abcde
```

```
REDIS_URL = redis://localhost:6379
```

---

### STEP 6: Deploy!

1. Click **"Create Web Service"** (bottom of page)
2. **WAIT 5-10 MINUTES** ⏰
3. You'll see: "Your service is live at: https://jats-backend-XXXXX.onrender.com"

**👉 Copy this URL when it appears**

---

## ✅ STEP 7: Update Vercel Frontend

Once backend is deployed:

1. Go to: https://vercel.com/dashboard
2. Click your `job-application-tracking-system` project
3. Go to **Settings** → **Environment Variables**
4. Find `VITE_API_URL`
5. Update to:
   ```
   https://jats-backend-XXXXX.onrender.com/api/v1
   ```
   (Replace XXXXX with your actual Render backend URL)
6. Click **Save**

---

## ✅ STEP 8: Redeploy Vercel

1. Go to **Deployments** tab
2. Click the latest deployment
3. Click **"..."** menu → **"Redeploy"**
4. **WAIT 2-3 MINUTES**

---

## ✅ STEP 9: Test Everything!

1. Go back to your app: https://job-application-tracking-system-XXXX.vercel.app/login
2. Do a **hard refresh**: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)
3. The "Failed to fetch" errors should be **GONE** ✅
4. Try signing up:
   - Username: `testuser`
   - Email: `test@example.com`
   - Role: `Software Developer`
   - Password: `test123`

---

## 📋 Checklist

- [ ] 1. Clicked "New +" on Render
- [ ] 2. Selected "Web Service"
- [ ] 3. Connected GitHub repo
- [ ] 4. Set name: `jats-backend`
- [ ] 5. Set region: `Singapore`
- [ ] 6. Set root directory: `backend`
- [ ] 7. Set build command: `pip install -r requirements.txt`
- [ ] 8. Set start command: `cd backend && uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT`
- [ ] 9. Added ALL 6 environment variables
- [ ] 10. Clicked "Create Web Service"
- [ ] 11. Waited for deployment (5-10 min)
- [ ] 12. Copied backend URL
- [ ] 13. Updated Vercel VITE_API_URL
- [ ] 14. Redeployed Vercel
- [ ] 15. Did hard refresh in browser
- [ ] 16. Tested signup/login ✅

---

## ⚠️ IMPORTANT NOTES

✅ **Database region:** Singapore (matches your DB region - GOOD!)
✅ **Backend deployment time:** 5-10 minutes (be patient!)
✅ **Environment variables:** Copy EXACTLY as shown
✅ **Hard refresh:** Essential - do `Ctrl+Shift+R`

---

## 🆘 If Something Goes Wrong

### "Build Failed" Error:
1. Check Render logs (click service → Logs)
2. Make sure Python version is set to 3.12
3. Check that DATABASE_URL is correct

### "Connection refused" Error:
1. DATABASE_URL might be wrong
2. Try copying the exact value again from Render

### Still getting "Failed to fetch":
1. Wait 5 more minutes (backend might still be starting)
2. Check that VITE_API_URL is correct in Vercel
3. Did you redeploy Vercel? (essential!)

---

## 🎉 You're Almost There!

After these steps, your app will be:
- ✅ Frontend on Vercel (fast, global)
- ✅ Backend on Render (Singapore)
- ✅ Database on Render (Singapore)
- ✅ Login/Signup working
- ✅ Fully functional! 🚀

---

**Ready? Go to Render and start with STEP 1. Tell me when the backend is deployed!** 👉
