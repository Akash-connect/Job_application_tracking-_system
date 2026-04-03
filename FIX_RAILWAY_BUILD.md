# Fix Railway Build Error - Step by Step

## What went wrong?
Railway couldn't parse the build configuration. This happens when:
- Root directory is set incorrectly
- Build command is missing
- Service isn't properly linked to a specific directory

## How to Fix

### Step 1: Push the Configuration Files

```bash
git add backend/railway.toml backend/Procfile railway.json .railwayignore
git commit -m "Add Railway configuration files"
git push origin main
```

### Step 2: Delete the Failed Service in Railway

1. Go to https://railway.app
2. Select your **production** project
3. Click on the failed **Job_application_tracking-system** service
4. Click **Settings** (gear icon)
5. Scroll to **Danger Zone**
6. Click **Delete Service**
7. Confirm deletion

### Step 3: Remove the GitHub Connection (Optional)

1. In Railway project settings
2. Under **Repo** section
3. Click **Disconnected** (if still connected)

### Step 4: Create New FastAPI Service - Correct Way

**Option A: Using Railway CLI (Recommended)**

```bash
# Install Railway CLI
npm install -g @railway/cli
# or
brew install railway  # macOS

# Login
railway login

# Link to project
railway link <YOUR_PROJECT_ID>

# Add service
railway add
# Select: Create new service
# Name: fastapi-api
# Choose: Python
```

**Option B: Using Railway Dashboard**

1. Go to your **production** project
2. Click **Create** or **Add Service**
3. Select **GitHub Repo**
4. Choose your **Job_application_tracking-system** repo
5. ⚠️ **IMPORTANT - Root Directory: Set to `backend/`**
6. Go to **Variables** tab and add:
   ```
   PYTHONPATH=/app/backend:/app/backend/django_app
   DJANGO_SETTINGS_MODULE=config.settings
   ```

### Step 5: Add PostgreSQL Service (If not already added)

1. Click **Create** or **Add Service**
2. Search for **PostgreSQL**
3. Click **Create**
4. Railway auto-creates database
5. Copy the `DATABASE_URL` from **Variables**

### Step 6: Add Redis Service (If not already added)

1. Click **Create** or **Add Service**
2. Search for **Redis**
3. Click **Create**
4. Copy the `REDIS_URL` from **Variables**

### Step 7: Configure FastAPI Service Variables

In Railway Dashboard → Your **fastapi-api** service → **Variables**:

```
DATABASE_URL=<from PostgreSQL service>
REDIS_URL=<from Redis service>
POSTGRES_HOST=<extract from DATABASE_URL>
POSTGRES_PORT=5432
POSTGRES_DB=jats
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<extract from DATABASE_URL>
JWT_SECRET_KEY=<from your .env file>
DJANGO_SECRET_KEY=<from your .env file>
FASTAPI_PORT=$PORT
NODE_ENV=production
```

### Step 8: Configure Build & Start Commands

In Railway Dashboard → Your **fastapi-api** service → **Settings**:

**Build Command:**
```bash
pip install -r requirements.txt
```

**Start Command:**
```bash
uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT
```

### Step 9: Deploy

1. Railway should auto-trigger a build
2. Watch the **Deployment** logs
3. You should see: "✅ Deployment successful"

### Step 10: Get Your Backend URL

1. Go to **Networking** tab
2. Copy the public URL (e.g., `https://your-backend-xxxx.railway.app`)
3. Update this in Vercel frontend's `VITE_API_URL` environment variable

---

## If Still Getting Build Error

### Check Build Logs:

1. In Railway → Your service
2. Click **Deployments** tab
3. Click on the failed deployment
4. Click **View logs**
5. Look for error messages

### Common Issues:

**"ModuleNotFoundError: No module named 'config'"**
→ Make sure `PYTHONPATH=/app/backend:/app/backend/django_app` is set

**"No start command found"**
→ Make sure Start Command is set to:
```bash
uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT
```

**"Root Directory not found"**
→ Set Root Directory to `backend/` (not `./backend`)

### Nuclear Option - Recreate Everything

If still failing, start fresh:

```bash
# 1. In Railway, delete the project
# 2. Create new project
# 3. Add PostgreSQL service
# 4. Add Redis service
# 5. Add GitHub service (backend/)
# 6. Set all environment variables
# 7. Deploy
```

---

## Verification

After deployment succeeds, test your backend:

```bash
# Replace with your Railway URL
curl https://your-backend-xxxx.railway.app/health
# Should return: {"status":"ok"}
```

If you get `{"status":"ok"}`, your backend is working! ✅

---

## Next: Update Vercel Frontend

Once backend is running, update Vercel:

1. Go to https://vercel.com → Your project
2. Settings → Environment Variables
3. Update:
   ```
   VITE_API_URL: https://your-backend-xxxx.railway.app/api/v1
   ```
4. Redeploy

Your full stack should now be working! 🚀
