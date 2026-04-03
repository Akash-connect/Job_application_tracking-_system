# Job Application Tracking System - Deployment Guide

## Option 1: Vercel (Frontend Only) + Railway/Render (Backend)

### Frontend Deployment on Vercel

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to https://vercel.com/new
   - Import your GitHub repository
   - Set Root Directory to `./frontend`
   - Add Environment Variables:
     - `VITE_API_URL`: Your backend API URL (e.g., `https://your-backend.railway.app/api/v1`)

3. **Deploy**
   - Vercel will automatically deploy on every git push to main

### Backend Deployment on Railway

**1. Prepare Backend for Railway**

Create `railway.json`:
```json
{
  "reference": "https://railway.app"
}
```

**2. Create PostgreSQL Database on Railway**
   - Create new project
   - Add PostgreSQL service
   - Copy DATABASE_URL

**3. Create Redis Cache on Railway**
   - Add Redis service to same project
   - Copy REDIS_URL

**4. Deploy FastAPI Service**
   - Add new service → Connect GitHub repo
   - Root Directory: `./backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     ```
     DATABASE_URL=<from PostgreSQL>
     REDIS_URL=<from Redis>
     POSTGRES_HOST=<from DATABASE_URL>
     POSTGRES_PORT=5432
     POSTGRES_DB=jats
     POSTGRES_USER=<from DATABASE_URL>
     POSTGRES_PASSWORD=<from DATABASE_URL>
     JWT_SECRET_KEY=<generate-secure-key>
     VITE_API_URL=https://<your-vercel-app>.vercel.app
     ```

**5. Deploy Django Service** (Optional for Admin)
   - Add another service for Django
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `sh scripts/start-django.sh`
   - Same environment variables

---

## Option 2: Full-Stack on Railway (Recommended)

Railway supports both frontend and backend in a single project.

### Steps:

1. **Create Railway Project**
   - Go to https://railway.app
   - Create new project

2. **Add Services**
   ```bash
   # PostgreSQL
   Add PostgreSQL service
   
   # Redis
   Add Redis service
   
   # Backend (FastAPI)
   Connect GitHub repo → Select backend/
   
   # Frontend
   Connect GitHub repo → Select frontend/
   ```

3. **Configure Environment Variables**
   - Set all required env vars (see `.env.example`)

4. **Deploy**
   - Railway auto-deploys on git push

---

## Option 3: Docker on AWS/GCP/Azure

Use Docker Compose as-is but deploy to:
- AWS ECS
- Google Cloud Run
- Azure Container Instances
- DigitalOcean App Platform

---

## Environment Variables for Production

Create `.env.production`:
```env
# Frontend
VITE_API_URL=https://your-backend-domain.com/api/v1

# FastAPI
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8000
JWT_SECRET_KEY=<generate-with-openssl-rand-hex-32>
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=120

# Django
DJANGO_SECRET_KEY=<generate-secure-key>
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=<secure-password>

# Database
DATABASE_URL=postgresql://user:password@host:5432/jats
POSTGRES_HOST=<host>
POSTGRES_PORT=5432
POSTGRES_DB=jats
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>

# Redis
REDIS_URL=redis://:password@host:6379/0

# CORS
CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
```

---

## Files to Add for Production

1. `.dockerignore` - Optimize Docker builds
2. `Dockerfile.prod` - Production-optimized Docker image
3. `nginx.conf.prod` - Production nginx config
4. `docker-compose.prod.yml` - Production compose file

---

## Recommended Services

| Component | Free Tier | Paid Starting |
|-----------|-----------|---------------|
| Frontend | Vercel | $20/month |
| Backend | Railway | $5/month |
| Database | Railway PostgreSQL | $15/month |
| Redis | Railway Redis | $5/month |
| **Total** | **$0 (with limits)** | **~$45/month** |

---

## Quick Start Steps

### To Deploy on Vercel + Railway:

```bash
# 1. Create GitHub repository
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main

# 2. Go to Vercel
# - Import GitHub repo
# - Set root directory to /frontend
# - Add VITE_API_URL environment variable
# - Deploy ✅

# 3. Go to Railway
# - Create project
# - Add PostgreSQL service
# - Add Redis service
# - Import GitHub repo for backend
# - Set environment variables
# - Deploy ✅
```

---

## Troubleshooting

**CORS Errors on Production**
→ Update FastAPI CORS origins

**Database Connection Failed**
→ Add IP whitelist in Railway
→ Verify DATABASE_URL format

**Frontend Can't Reach API**
→ Check VITE_API_URL environment variable
→ Ensure API port is exposed

**Port Conflicts**
→ Use $PORT environment variable in start command
