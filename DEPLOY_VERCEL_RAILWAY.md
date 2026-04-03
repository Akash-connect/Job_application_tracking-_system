# Deploy to Vercel + Railway - Step by Step Guide

## Part 1: Prepare Your Code (Local)

### Step 1: Generate Production Environment Variables

```bash
# On macOS/Linux
chmod +x scripts/generate-prod-env.sh
./scripts/generate-prod-env.sh

# On Windows PowerShell
bash scripts/generate-prod-env.sh
```

This will create `.env.production` with secure keys. **Edit and update:**
- `DJANGO_ALLOWED_HOSTS`
- `DJANGO_SUPERUSER_EMAIL`
- `POSTGRES_HOST`
- `POSTGRES_PASSWORD`
- `REDIS_URL` 
- `VITE_API_URL`

### Step 2: Initialize Git Repository

```bash
git init
git add .
git commit -m "Initial commit - JATS production ready"
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## Part 2: Deploy Backend on Railway

### Step 1: Sign Up & Create Project

1. Go to https://railway.app
2. Sign up with GitHub (recommended)
3. Click "Create New Project"

### Step 2: Add PostgreSQL Database

1. Click "Add Service" → Search "PostgreSQL"
2. Select "PostgreSQL"
3. Railway creates the database automatically
4. Note the connection details

### Step 3: Add Redis Cache (Optional but Recommended)

1. Click "Add Service" → Search "Redis"
2. Select "Redis"
3. Railway provides Redis URL automatically

### Step 4: Deploy FastAPI Backend

1. Click "Add Service" → "GitHub Repo"
2. Select your JATS repository
3. Set these variables:
   ```
   Service Name: fastapi-api
   Root Directory: backend
   ```

4. Go to "Variables" tab and add:
   ```
   DATABASE_URL: postgresql://....  (from PostgreSQL service)
   REDIS_URL: redis://....  (from Redis service)
   JWT_SECRET_KEY: (from .env.production)
   DJANGO_SECRET_KEY: (from .env.production)
   POSTGRES_HOST: (from DATABASE_URL)
   POSTGRES_PORT: 5432
   POSTGRES_DB: jats
   POSTGRES_USER: postgres
   POSTGRES_PASSWORD: (from DATABASE_URL password)
   FASTAPI_PORT: $PORT
   NODE_ENV: production
   ```

5. Go to "Build" tab:
   ```
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT
   ```

6. Click "Deploy" - Railway will auto-deploy from GitHub

### Step 5: Get Backend URL

- After deployment, Railway shows: `https://your-backend-xxxx.railway.app`
- Copy this URL - you'll need it for frontend

---

## Part 3: Deploy Frontend on Vercel

### Step 1: Go to Vercel

1. Visit https://vercel.com
2. Sign up with GitHub
3. Click "Add New Project"

### Step 2: Import Repository

1. Click "Import Git Repository"
2. Select your JATS repository
3. Click "Import"

### Step 3: Configure Project

1. **Framework Preset:** Select "Vite"
2. **Root Directory:** Select `frontend/`
3. **Build Command:** `npm run build`
4. **Output Directory:** `dist`
5. **Install Command:** `npm install`

### Step 4: Add Environment Variables

1. Go to "Environment Variables" section
2. Add:
   ```
   VITE_API_URL: https://your-backend-xxxx.railway.app/api/v1
   ```
   (Replace with your actual Railway API URL from Step 5 above)

3. Click "Deploy"

### Step 5: Get Frontend URL

- After deployment: `https://your-project.vercel.app`
- Your app is now live! 🎉

---

## Part 4: Update CORS (Backend)

Since your frontend is now on `your-project.vercel.app`, update FastAPI CORS:

1. Edit file: `backend/fastapi_service/main.py`

2. Update the CORS configuration:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://your-project.vercel.app",  # ADD THIS
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

3. Push to GitHub:
```bash
git add backend/fastapi_service/main.py
git commit -m "Update CORS for production URL"
git push
```

4. Railway auto-redeploys ✅

---

## Part 5: Verify Everything Works

### Test Login Page

1. Visit `https://your-project.vercel.app`
2. You should see the login page
3. Try creating an account or logging in with:
   - Email: `admin@yourdomain.com` (from env)
   - Password: Create or use pre-configured one

### If "Failed to Fetch" Error

**Troubleshooting:**

1. Check browser console (F12 → Console tab)
2. Verify `VITE_API_URL` is correct in Vercel environment
3. Ensure Railway backend is running:
   ```bash
   curl https://your-backend-xxxx.railway.app/health
   ```
   Should return: `{"status":"ok"}`

4. Check CORS in Railway logs

---

## Part 6: Database Initialization (First Time Only)

After first deployment, run migrations on Railway:

### Option A: Using Railway Dashboard

1. Go to Railway Project
2. Select FastAPI Service
3. Click "Deployments"
4. Open the active deployment
5. Go to "Logs"
6. Manually run (in Railway CLI):
   ```bash
   railway exec "python /app/backend/django_app/manage.py migrate"
   ```

### Option B: Using Railway CLI

```bash
npm install -g @railway/cli
railway login
railway link <PROJECT_ID>
railway exec "python /app/backend/django_app/manage.py migrate"
railway exec "python /app/backend/django_app/manage.py seed_sample_data"
```

---

## Part 7: Custom Domain Setup (Optional)

### Add Domain to Vercel Frontend

1. In Vercel Dashboard → Select project
2. Go to "Settings" → "Domains"
3. Add your custom domain (e.g., `app.yourdomain.com`)
4. Follow DNS setup instructions

### Add Domain to Railway Backend

1. In Railway → Select FastAPI service
2. Go to "Settings" → "Custom Domain"
3. Add API domain (e.g., `api.yourdomain.com`)
4. Update DNS records

### Update Frontend Environment Variable

In Vercel → Environment Variables:
```
VITE_API_URL: https://api.yourdomain.com/api/v1
```

---

## Estimated Costs (Monthly)

| Service | Tier | Cost |
|---------|------|------|
| Vercel | Hobby (free) | $0 |
| Vercel | Pro | $20 |
| Railway | Free tier | $0-5 |
| Railway | Usage-based | ~$10-50 |
| **Total** | | **$0-70** |

---

## Summary

✅ Frontend deployed on Vercel
✅ Backend deployed on Railway
✅ Database on Railway PostgreSQL
✅ Redis on Railway
✅ Custom domains ready
✅ Auto-deploy on git push

Your application is now production-ready! 🚀
