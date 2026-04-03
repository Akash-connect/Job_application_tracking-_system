"""FastAPI application entrypoint."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import bootstrap  # noqa: F401
from .api.auth import router as auth_router
from .api.jobs import router as jobs_router
from .core.config import settings

app = FastAPI(
    title="Job Application Tracking System API",
    version="1.0.0",
    description="REST API for tracking applications, analytics, follow-ups, and workflow automation.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:8000",
        "http://localhost:8001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix=settings.api_prefix)
app.include_router(jobs_router, prefix=settings.api_prefix)


@app.get("/health", tags=["system"])
def healthcheck():
    """Basic service health endpoint."""
    return {"status": "ok"}
