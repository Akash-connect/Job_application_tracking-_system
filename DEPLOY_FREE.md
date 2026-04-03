# Deploy JATS Completely FREE 🎉

## Best Free-Tier Options

| Platform | Frontend | Backend | Database | Redis | Total Cost |
|----------|----------|---------|----------|-------|-----------|
| **Vercel + Render** | FREE ✅ | FREE ✅ | FREE ✅ | Included | **$0** |
| **Vercel + Railway** | FREE ✅ | $5 credit | FREE ✅ | FREE ✅ | **$0** (limited) |
| **GitHub Pages + Render** | FREE ✅ | FREE ✅ | FREE ✅ | Included | **$0** |

---

## 🥇 BEST FREE OPTION: Vercel + Render

### Why This Combo?
- ✅ Both have **unlimited free tier**
- ✅ No credit card required for Vercel
- ✅ Render includes PostgreSQL + Redis
- ✅ No sleep mode or restrictions
- ✅ Professional managed services

---

## 📋 Step-by-Step: FREE Deployment

### PART 1: Deploy Frontend on Vercel (FREE)

**Step 1: Go to Vercel**

1. Visit https://vercel.com
2. Click "Sign Up" → Choose "Continue with GitHub"
3. Authorize GitHub access
4. Accept terms

**Step 2: Import Your Project**

1. Click "Add New Project"
2. Click "Import Git Repository"
3. Find your repo: `Job_application_tracking-_system`
4. Click "Import"

**Step 3: Configure**

1. **Framework Preset:** Select "Vite"
2. **Root Directory:** Select `frontend/`
3. **Build Command:** Should auto-fill `npm run build`
4. **Install Command:** Should auto-fill `npm install`
5. **Output Directory:** Should auto-fill `dist`
6. Click "Deploy"

Wait for deployment to complete (~2 minutes)

**Step 4: After Deployment**

1. You'll see a URL like: `https://your-project-xxxxx.vercel.app`
2. Copy this URL - you'll need it later
3. ✅ Frontend is now LIVE!

---

### PART 2: Deploy Backend on Render (FREE)

**Step 1: Go to Render**

1. Visit https://render.com
2. Click "Get Started"
3. Choose "Sign up with GitHub"
4. Authorize and accept terms

**Step 2: Create Web Service**

1. Click "New +" button
2. Select "Web Service"
3. Select "GitHub"
4. Find your repo: `Job_application_tracking-_system`
5. Click "Connect"

**Step 3: Configure Service**

Fill in these settings:

```
Name: jats-backend
Environment: Python 3
Region: Choose closest to you
Branch: main
Build Command: pip install -r requirements.txt
Start Command: cd backend && uvicorn fastapi_service.main:app --host 0.0.0.0 --port $PORT
```

**Step 4: Add Environment Variables**

Click "Advanced" → "Add Environment Variable" and add:

```
PYTHONPATH=/var/task/backend:/var/task/backend/django_app
DJANGO_SETTINGS_MODULE=config.settings
FASTAPI_PORT=$PORT
DJANGO_DEBUG=False
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=120
```

**Step 5: Create PostgreSQL Database**

1. Go back to Render dashboard
2. Click "New +" → "PostgreSQL"
3. Name: `jats-db`
4. Region: Same as your web service
5. Click "Create Database"
6. Wait for creation (2-3 minutes)

**Step 6: Copy Database Credentials**

1. When PostgreSQL is ready, open the service
2. Copy these variables from "Connections" section:
   - `DATABASE_URL` (full URL)
   - `POSTGRES_HOST`
   - `POSTGRES_PORT`
   - `POSTGRES_USER`
   - `POSTGRES_PASSWORD`

**Step 7: Add Database to Backend Service**

1. Go back to your **jats-backend** service
2. Click "Environment"
3. Add variables:

```
DATABASE_URL=<copied from PostgreSQL>
POSTGRES_HOST=<copied from PostgreSQL>
POSTGRES_PORT=5432
POSTGRES_DB=jats
POSTGRES_USER=<copied from PostgreSQL>
POSTGRES_PASSWORD=<copied from PostgreSQL>
JWT_SECRET_KEY=your-secret-key-min-32-chars-make-it-random
DJANGO_SECRET_KEY=your-django-secret-key-min-50-chars-make-it-random
```

**Step 8: Create Backend Service**

1. From the Web Service screen
2. Click "Create Web Service"
3. Wait for build and deployment (5-10 minutes)

**Step 9: Get Backend URL**

1. From Render dashboard → jats-backend service
2. Copy your backend URL: `https://your-backend-xxxx.onrender.com`
3. ✅ Backend is now LIVE!

---

### PART 3: Connect Frontend to Backend

**Update Vercel with Backend URL**

1. Go to Vercel dashboard → Your frontend project
2. Click "Settings" → "Environment Variables"
3. Add new variable:
   ```
   VITE_API_URL: https://your-backend-xxxx.onrender.com/api/v1
   ```
4. Click "Save"
5. Go to "Deployments"
6. Click the latest deployment
7. Click "Redeploy"

Wait 1-2 minutes for redeploy.

---

### PART 4: Test Your App! 🎉

1. Visit your Vercel frontend URL
2. You should see the login page
3. Try creating an account or login with:
   - Email: `admin@example.com`
   - Password: `admin12345` (from your env)

If you see the dashboard → **Congratulations!** Your app is live! 🚀

---

## 🆓 Free Tier Limits

### Vercel
- ✅ Unlimited deployments
- ✅ Unlimited projects
- ✅ Unlimited bandwidth
- ✅ No downtime
- ✅ Custom domains (paid)

### Render
- ✅ Free tier web service (shared CPU)
- ✅ Unlimited PostgreSQL size
- ✅ Auto-sleep after 15 min inactivity (but NO ISSUE for APIs)
- ✅ Automatic wake-up on request
- ⚠️ Cold start (5-10 seconds first request)

### Important: Render Limitations
- **Free instances sleep after 15 minutes of inactivity**
- When you call the API, it wakes up (takes 5-10 seconds)
- For production, upgrade to paid ($7+/month)
- For development/learning, free tier is fine

---

## 💪 Dealing with Render Sleep Mode

**Option 1: Keep It Awake (Ping Service)**

Add a cron job to ping your backend every 14 minutes:

```bash
# Using external free service like kaffeine.herokuapp.com (needs replacement)
# Or use GitHub Actions (free):
```

Create `.github/workflows/uptime.yml`:
```yaml
name: Keep Render Alive
on:
  schedule:
    - cron: "*/14 * * * *"

jobs:
  ping:
    runs-on: ubuntu-latest
    steps:
      - name: Ping backend
        run: |
          curl -f https://your-backend-xxxx.onrender.com/health || exit 1
```

**Option 2: Upgrade to Paid ($7/month)**

Go to Render → Your service → "Convert to Paid"

---

## 🔒 Security for Production

Your app is now public! Secure it:

### 1. Change Default Credentials

In your `.env` file (local only):
```
DJANGO_SUPERUSER_EMAIL=your-email@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=<super-secure-random-password>
```

Update Render environment variables:
1. Go to Render → jats-backend
2. Click "Environment"
3. Update the secrets
4. Redeploy

### 2. Generate Secure Keys

On your local machine:
```bash
# Generate random secrets
python -c "import secrets; print(secrets.token_urlsafe(32))"  # JWT_SECRET_KEY
python -c "import secrets; print(secrets.token_urlsafe(50))"  # DJANGO_SECRET_KEY
```

Update these in Render environment variables.

### 3. Disable Debug Mode in Production

Already done! (DJANGO_DEBUG=False in environment)

---

## 📊 Cost Breakdown

| Service | Fee | Notes |
|---------|-----|-------|
| Vercel Frontend | $0 | Unlimited |
| Render Backend | $0 | Free tier (shared resources) |
| Render PostgreSQL | $0 | Unlimited |
| **Total** | **$0** | ✅ Completely FREE |

---

## ⚡ Performance Tips

Since using free tier:

1. **Accept 5-10 second cold start** on first request
2. **Keep ping service running** to prevent sleep
3. **Monitor usage** - stick to free limits
4. **Cache responses** in frontend to reduce API calls
5. **Use pagination** for large data sets

---

## 📈 When to Upgrade

Upgrade your Render backend to paid ($7/month) when:
- ✅ You have paying customers
- ✅ You need 24/7 uptime (no sleep)
- ✅ You get more than 100 requests/day
- ✅ You want faster response times
- ✅ Better for production use

---

## 🎯 Next Steps

1. **Deploy Frontend on Vercel** (15 minutes)
2. **Deploy Backend on Render** (20 minutes)
3. **Connect them** (5 minutes)
4. **Test your app** (5 minutes)
5. **Total time: ~45 minutes** ⏱️

## ✅ Deployment Checklist

- [ ] Push to GitHub
- [ ] Sign up for Vercel
- [ ] Deploy frontend
- [ ] Sign up for Render
- [ ] Create PostgreSQL database
- [ ] Deploy backend
- [ ] Connect frontend to backend
- [ ] Test login page
- [ ] Test create account
- [ ] View dashboard
- [ ] Celebrate! 🎉

---

## 🆘 Troubleshooting

### "Failed to Fetch" Error
1. Check if backend URL is correct in Vercel env
2. Curl the backend: `https://your-backend-xxxx.onrender.com/health`
3. Should return: `{"status":"ok"}`
4. If not, check Render logs for errors

### "Internal Server Error" on Login
1. Check Render PostgreSQL is running
2. Verify DATABASE_URL is set correctly
3. Check Render logs: "Logs" tab in service
4. Run migrations if needed

### Backend Takes Too Long to Respond
- Normal for first request (cold start)
- Set up ping service to keep it warm
- Or upgrade to paid tier

---

## 🚀 Final Result

After following this guide:

✅ Frontend running globally on Vercel  
✅ Backend running on Render  
✅ Database on Render PostgreSQL  
✅ Everything connected and working  
✅ Total cost: **$0** 💰  
✅ Deployment time: **~45 minutes** ⏱️

Your **Job Application Tracking System** is now live on the internet! 🌐

Share your Vercel frontend URL with anyone to use your app!

---

## 📚 Resources

- Vercel Docs: https://vercel.com/docs
- Render Docs: https://render.com/docs
- PostgreSQL Docs: https://www.postgresql.org/docs/

---

**Questions?** Check the troubleshooting section above or the main deployment guides:
- `DEPLOY_VERCEL_RAILWAY.md` - For Railway option
- `DEPLOYMENT_ALTERNATIVES.md` - For other options
- `FIX_RAILWAY_BUILD.md` - If Railway issues
