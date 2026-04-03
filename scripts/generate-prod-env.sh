#!/bin/bash

# Generate secure keys for production
echo "🔐 Generating secure keys for production..."

# Generate Django Secret Key
DJANGO_SECRET_KEY=$(openssl rand -hex 32)

# Generate JWT Secret Key  
JWT_SECRET_KEY=$(openssl rand -hex 32)

# Generate Database Password
DB_PASSWORD=$(openssl rand -hex 16)

# Generate Redis Password
REDIS_PASSWORD=$(openssl rand -hex 16)

echo ""
echo "✅ Generated Keys (copy these to your .env.production)"
echo "=================================================="
echo ""
echo "DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY"
echo "JWT_SECRET_KEY=$JWT_SECRET_KEY"
echo "POSTGRES_PASSWORD=$DB_PASSWORD"
echo "REDIS_PASSWORD=$REDIS_PASSWORD"
echo ""
echo "💾 Saving to .env.production..."

cat > .env.production << EOF
# Django
DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=yourdomain.com,api.yourdomain.com
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=change-me-in-production

# Database
POSTGRES_DB=jats
POSTGRES_USER=jats_user
POSTGRES_PASSWORD=$DB_PASSWORD
POSTGRES_HOST=your-database-host
POSTGRES_PORT=5432
DATABASE_URL=postgresql://jats_user:$DB_PASSWORD@your-database-host:5432/jats

# Redis
REDIS_URL=redis://:$REDIS_PASSWORD@your-redis-host:6379/0

# FastAPI
FASTAPI_HOST=0.0.0.0
FASTAPI_PORT=8001
JWT_SECRET_KEY=$JWT_SECRET_KEY
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=120

# Frontend
VITE_API_URL=https://api.yourdomain.com/api/v1
EOF

echo "✅ File created at .env.production"
echo "⚠️  Remember to update the host, domain, and email values"
