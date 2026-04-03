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

export PYTHONPATH=/app/backend:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=config.settings
cd /app/backend/django_app
python manage.py migrate
python manage.py shell -c "from django.contrib.auth import get_user_model; import os; User=get_user_model(); email=os.getenv('DJANGO_SUPERUSER_EMAIL', 'admin@example.com'); password=os.getenv('DJANGO_SUPERUSER_PASSWORD', 'admin12345'); username=email.split('@')[0]; User.objects.filter(username=username).exists() or User.objects.create_superuser(username=username, email=email, password=password)"
python manage.py seed_sample_data
python manage.py runserver 0.0.0.0:8000

