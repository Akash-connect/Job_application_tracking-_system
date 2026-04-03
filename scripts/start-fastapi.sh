#!/bin/sh
set -e

# Wait for PostgreSQL to be ready
counter=0
while [ $counter -lt 60 ]; do
  python -c "import psycopg; psycopg.connect('postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB')" 2>/dev/null && break
  echo "Waiting for PostgreSQL... ($counter/60)"
  sleep 1
  counter=$((counter+1))
done

echo "PostgreSQL is ready!"

export PYTHONPATH=/app/backend:/app/backend/django_app:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=config.settings
cd /app/backend
uvicorn fastapi_service.main:app --host 0.0.0.0 --port 8001

