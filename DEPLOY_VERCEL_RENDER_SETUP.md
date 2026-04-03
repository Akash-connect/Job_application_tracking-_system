# 🚀 Complete Deployment Guide: Vercel + Render

## ✅ Pre-Deployment Checklist

- ✅ Code committed to GitHub: `https://github.com/Akash-connect/Job_application_tracking-_system`
- ✅ vercel.json configured
- ✅ Procfile configured for Render
- ✅ requirements.txt updated
- ✅ Environment variables documented

**You're ready to deploy!** 🎉

---

## STEP 1: Deploy Frontend on Vercel (10 minutes)

### 1.1 Go to Vercel

1. Open https://vercel.com
2. Click **"Sign up"**
3. Choose "Continue with GitHub"
4. Authorize Vercel to access your GitHub

### 1.2 Import Your Project

1. Click **"New Project"**
2. Click **"Import Git Repository"**
3. Find `Job_application_tracking-_system` and click **Import**

### 1.3 Configure Project

**Step 1: Set Root Directory**
- Current: `./` (default)
- Change to: `frontend/`
- Click the dropdown and select `frontend`

**Step 2: Add Environment Variables**

Click **"Environment Variables"** and add:

| Name | Value |
|------|-------|
| `VITE_API_URL` | `http://localhost:8001/api/v1` |

(We'll update this later with the actual Render URL)

**Step 3: Verify Build Settings**

- Build Command: `npm run build` ✅
- Output Directory: `dist` ✅
- Framework: `Vite` ✅

### 1.4 Deploy

Click **"Deploy"**

**Wait 3-5 minutes for deployment to complete**

You'll see:
```
✓ Deployment complete
Your site is live at: https://your-project-xxxx.vercel.app
```

**Save this URL!** You'll need it later.

---

## STEP 2: Set Up Database on Render (5 minutes)

### 2.1 Create Render Account

1. Open https://render.com
2. Click **"Sign up"**
3. Choose "Sign up with GitHub"
4. Authorize Render

### 2.2 Create PostgreSQL Database

1. Click **"New +"** (top right)
2. Select **"PostgreSQL"**
3. Fill in details:

| Field | Value |
|-------|-------|
| **Name** | `jats-database` |
| **Database** | `jats_db` |
| **User** | `jats_user` |
| **Region** | Choose closest to you |
| **PostgreSQL Version** | 16 |

4. Click **"Create Database"**

**Wait 2-3 minutes for database to initialize**

### 2.3 Save Database Credentials

After database is created, you'll see connection details:

```
Connection String:
postgresql://jats_user:XXXXXXXXXXXX@dpg-xxxxx.oregon-postgres.render.com:5432/jats_db

Internal Database URL:
postgresql://jats_user:XXXXXXXXXXXX@localhost:5432/jats_db
```

**Copy the full connection string!** You'll need it for the backend.

---

## STEP 3: Deploy Backend on Render (15 minutes)

### 3.1 Go Back to Render Dashboard

1. Click **"New +"**
2. Select **"Web Service"**
3. Click **"Build and deploy from a Git repository"**

### 3.2 Connect GitHub

1. Click **"Connect Account"** (if not connected)
2. Find and select `Job_application_tracking-_system`
3. Click **"Connect"**

### 3.3 Configure Backend Service

**Basic Settings:**

| Field | Value |
|-------|-------|
| **Name** | `jats-backend` |
| **Region** | Same as database |
| **Branch** | `main` |
| **Root Directory** | `backend` |

**Build Settings:**

| Field | Value |
|-------|-------|
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `cd backend && uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT` |

### 3.4 Add Environment Variables

Click **"Advanced"** → **"Add Secret File"** (or Environment Variables)

Add these variables:

```
DATABASE_URL=postgresql://jats_user:XXXXXXXXXXXX@dpg-xxxxx.oregon-postgres.render.com:5432/jats_db
DJANGO_SETTINGS_MODULE=config.settings
PYTHONPATH=/opt/render/project/src/backend:/opt/render/project/src/backend/django_app
JWT_SECRET_KEY=your_jwt_secret_key_here_generate_random_string
DJANGO_SECRET_KEY=your_django_secret_key_here_generate_random_string
REDIS_URL=redis://localhost:6379
```

**Generate Secret Keys** (generate random strings):
- For JWT_SECRET_KEY: Use https://openssl.rand -hex 32 (or create any 32-char random string)
- For DJANGO_SECRET_KEY: Use Django's: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

Or just use simple strings like:
```
JWT_SECRET_KEY=my_super_secret_jwt_key_12345
DJANGO_SECRET_KEY=my_django_secret_key_abcde
```

### 3.5 Deploy

1. Verify all settings
2. Click **"Create Web Service"**

**Wait 5-10 minutes for deployment**

You'll see:
```
✓ Service deployed
Your site is live at: https://jats-backend-xxxx.onrender.com
```

**Save this URL!** You'll need it now.

---

## STEP 4: Update Frontend with Backend URL (5 minutes)

### 4.1 Go Back to Vercel

1. Go to https://vercel.com/dashboard
2. Click your `Job_application_tracking-_system` project
3. Go to **Settings** → **Environment Variables**

### 4.2 Update VITE_API_URL

1. Find `VITE_API_URL`
2. Change value from `http://localhost:8001/api/v1` to:

```
https://jats-backend-xxxx.onrender.com/api/v1
```

(Replace `xxxx` with your actual Render URL)

### 4.3 Redeploy

1. Go to **Deployments**
2. Click the latest deployment
3. Click **"Redeploy"**

**Wait 2-3 minutes for redeployment**

---

## STEP 5: Test Your Deployment (5 minutes)

### 5.1 Test Frontend

1. Go to your Vercel URL: `https://your-project-xxxx.vercel.app`
2. You should see the login page ✅

### 5.2 Test Backend

1. Go to: `https://jats-backend-xxxx.onrender.com/docs`
2. You should see FastAPI Swagger docs ✅

### 5.3 Test API Connection

In your browser, go to your Vercel URL and:

1. Try to login with any credentials
2. You should see an error from backend (this means connection works!)
3. Or if database has data, it should load

**Expected behavior:**
- ✅ Login page loads
- ✅ API calls go through (check browser DevTools → Network)
- ✅ Database queries work

---

## ✅ Deployment Complete!

Your app is now LIVE! 🎉

| Component | Location |
|-----------|----------|
| Frontend | https://your-project-xxxx.vercel.app |
| Backend API | https://jats-backend-xxxx.onrender.com |
| Database | Render PostgreSQL |
| API Docs | https://jats-backend-xxxx.onrender.com/docs |

---

## 🆘 Troubleshooting

### Issue: "Failed to fetch" on login

**Cause:** Backend URL not set correctly

**Fix:**
1. Verify VITE_API_URL is set in Vercel
2. Verify Render backend URL is correct
3. Redeploy frontend

### Issue: Render backend shows 502 error

**Cause:** Deployment failed or environment variables missing

**Fix:**
1. Check Render logs: Click service → Logs
2. Verify DATABASE_URL is set correctly
3. Check PYTHONPATH variable

### Issue: "Database connection refused"

**Cause:** DATABASE_URL is incorrect

**Fix:**
1. Copy full connection string from Render database page
2. Paste into Render backend environment variables
3. Redeploy backend

### Issue: Login doesn't work

**Cause:** 
- Database not initialized
- Environment variables not set
- Backend not connected

**Fix:**
1. Verify API calls work in DevTools
2. Check Render logs for errors
3. Verify DATABASE_URL in backend

---

## 📊 Expected Costs

| Service | Cost |
|---------|------|
| Vercel | FREE (forever) |
| Render PostgreSQL | FREE (14 days) then $15/month |
| Render Backend | FREE (with auto-sleep after 30 min) |
| **Total** | **$0-15/month** |

---

## 🎯 Next Steps

After deployment works:

1. ✅ Add sample data to database
2. ✅ Customize app for production
3. ✅ Add custom domain (optional)
4. ✅ Set up auto-deploy from GitHub
5. ✅ Monitor logs and performance

---

## 📞 Support

If something goes wrong:

1. Check Render logs: Service → Logs
2. Check Vercel logs: Deployments → click deployment
3. Check browser DevTools → Network tab for API errors
4. Read error messages carefully!

---

## 📚 Related Guides

- `DEPLOY_FREE.md` - Alternative setup
- `DEPLOY_FIREBASE.md` - Firebase option
- `DEPLOY_VERCEL_RAILWAY.md` - Railway option
- `VERCEL_QUICK_FIX.md` - Quick troubleshooting

---

**Ready? Follow the steps above in order and your app will be LIVE! 🚀**
