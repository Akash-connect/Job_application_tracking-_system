"""Job application CRUD and analytics endpoints."""

from fastapi import APIRouter, Depends, File, Form, Query, Response, UploadFile, status

from ..schemas.jobs import AnalyticsResponse, DashboardStats, JobCreate, JobResponse, JobUpdate, ResumeUploadResponse
from ..services.job_service import JobService
from ..utils.serializers import serialize_job, serialize_resume
from .dependencies import get_current_user

router = APIRouter(tags=["jobs"])
service = JobService()


@router.post("/jobs", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(payload: JobCreate, current_user=Depends(get_current_user)):
    """Create a job application."""
    job = service.create_job(user_id=current_user.id, payload=payload.model_dump())
    return serialize_job(job)


@router.get("/jobs", response_model=list[JobResponse])
def list_jobs(
    current_user=Depends(get_current_user),
    search: str | None = Query(default=None),
    status_filter: str | None = Query(default=None, alias="status"),
    tag: str | None = Query(default=None),
):
    """List job applications with search and filter support."""
    jobs = service.list_jobs(user_id=current_user.id, search=search, status_filter=status_filter, tag=tag)
    return [serialize_job(job) for job in jobs]


@router.put("/jobs/{job_id}", response_model=JobResponse)
def update_job(job_id: int, payload: JobUpdate, current_user=Depends(get_current_user)):
    """Update an existing application."""
    job = service.update_job(user_id=current_user.id, job_id=job_id, payload=payload.model_dump(exclude_unset=True))
    return serialize_job(job)


@router.delete("/jobs/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, current_user=Depends(get_current_user)):
    """Delete an application."""
    service.delete_job(user_id=current_user.id, job_id=job_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/analytics", response_model=AnalyticsResponse)
def analytics(current_user=Depends(get_current_user)):
    """Return chart-ready analytics."""
    return service.analytics(user_id=current_user.id)


@router.get("/dashboard-stats", response_model=DashboardStats)
def dashboard_stats(current_user=Depends(get_current_user)):
    """Return headline KPI values."""
    return service.dashboard_stats(user_id=current_user.id)


@router.get("/resumes", response_model=list[ResumeUploadResponse])
def list_resumes(current_user=Depends(get_current_user)):
    """List resumes available for attaching to applications."""
    return [serialize_resume(resume) for resume in service.list_resumes(user_id=current_user.id)]


@router.post("/resumes", response_model=ResumeUploadResponse, status_code=status.HTTP_201_CREATED)
def upload_resume(
    title: str = Form(...),
    version: str = Form(default=""),
    file: UploadFile = File(...),
    current_user=Depends(get_current_user),
):
    """Upload a resume asset for the current user."""
    resume = service.upload_resume(user_id=current_user.id, title=title, version=version, file=file)
    return serialize_resume(resume)
