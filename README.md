# Job Application Tracking System

Premium full-stack Job Application Tracking System (JATS) built with Django, FastAPI, PostgreSQL, Redis/Celery readiness, and a React + Tailwind frontend.

## Stack

- Django: authentication, admin panel, ORM models, media handling
- FastAPI: JWT-secured REST API, analytics, job tracking services, Swagger docs
- PostgreSQL: primary relational database
- Redis + Celery: optional background reminders
- React + Tailwind CSS: responsive premium dashboard UI

## Project Structure

```text
backend/
  django_app/
    accounts/
    jobs/
    config/
  fastapi_service/
    api/
    core/
    repositories/
    schemas/
    services/
    utils/
frontend/
  src/
    components/
    hooks/
    lib/
    pages/
    styles/
scripts/
docker-compose.yml
```

## Features

- Register and login with JWT authentication
- Django admin for users, companies, tags, resumes, and job applications
- Job CRUD with search and status filtering
- Dashboard stats and analytics charts
- Drag-and-drop kanban board
- Dark/light theme toggle
- Toast notifications and skeleton loading states
- Resume upload endpoints
- Seeded sample data for local development

## API Endpoints

Base URL: `http://localhost:8001/api/v1`

- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/me`
- `POST /jobs`
- `GET /jobs`
- `PUT /jobs/{id}`
- `DELETE /jobs/{id}`
- `GET /analytics`
- `GET /dashboard-stats`
- `GET /resumes`
- `POST /resumes`

Swagger docs are available at `http://localhost:8001/docs`.

## Environment Setup

1. Copy `.env.example` to `.env`
2. Adjust secrets and database values as needed

Recommended local defaults:

```env
POSTGRES_DB=jats
POSTGRES_USER=jats
POSTGRES_PASSWORD=jats
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
VITE_API_URL=http://localhost:8001/api/v1
```

## Local Development

### Backend

1. Create and activate a virtual environment
2. Install dependencies:

```bash
pip install -r backend/requirements.txt
```

3. Run Django migrations:

```bash
cd backend/django_app
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Seed sample data:

```bash
python manage.py seed_sample_data
```

6. Start Django admin:

```bash
python manage.py runserver 0.0.0.0:8000
```

7. Start FastAPI from a second terminal:

```bash
cd backend
uvicorn fastapi_service.main:app --reload --host 0.0.0.0 --port 8001
```

8. Optional Celery worker:

```bash
cd backend
celery -A django_app.celery_app worker --loglevel=info
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend URL: `http://localhost:5173`

## Docker

After creating `.env`, run:

```bash
docker compose up --build
```

Services:

- Django admin: `http://localhost:8000/admin`
- FastAPI: `http://localhost:8001`
- Swagger docs: `http://localhost:8001/docs`
- Frontend: `http://localhost:3000`

The Docker startup flow auto-runs migrations, creates a superuser from `.env`, and seeds demo data.

## Demo Credentials

- Demo user: `demo`
- Demo password: `demo12345`

Admin credentials are created from:

- `DJANGO_SUPERUSER_EMAIL`
- `DJANGO_SUPERUSER_PASSWORD`

## Notes

- Resume upload is available through the FastAPI `/resumes` endpoint and Django admin.
- Email reminders are scaffolded through a Celery task collector and can be extended with SMTP or a transactional email provider.
- Social login is intentionally left optional and not enabled by default.
