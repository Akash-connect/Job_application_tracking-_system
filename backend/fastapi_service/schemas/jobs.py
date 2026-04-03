"""Pydantic schemas for job tracking resources."""

from datetime import date, datetime

from pydantic import BaseModel, ConfigDict, Field


class CompanyPayload(BaseModel):
    """Input structure for company creation or reuse."""

    name: str = Field(min_length=2, max_length=180)
    website: str | None = None
    location: str | None = None
    notes: str | None = None


class ResumeSummary(BaseModel):
    """Serialized resume metadata."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    version: str | None = None
    file: str


class ResumeUploadResponse(BaseModel):
    """Response payload for an uploaded resume asset."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    version: str | None = None
    file: str


class CompanySummary(BaseModel):
    """Serialized company metadata."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    website: str | None = None
    location: str | None = None
    notes: str | None = None


class TagSummary(BaseModel):
    """Serialized tag metadata."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    color: str


class JobCreate(BaseModel):
    """Payload for creating a job application."""

    company: CompanyPayload
    role: str = Field(min_length=2, max_length=180)
    status: str = "applied"
    salary_min: int | None = None
    salary_max: int | None = None
    job_url: str | None = None
    notes: str | None = None
    application_date: date
    follow_up_date: date | None = None
    is_remote: bool = False
    tag_names: list[str] = []
    resume_id: int | None = None


class JobUpdate(BaseModel):
    """Payload for updating a job application."""

    company: CompanyPayload | None = None
    role: str | None = None
    status: str | None = None
    salary_min: int | None = None
    salary_max: int | None = None
    job_url: str | None = None
    notes: str | None = None
    application_date: date | None = None
    follow_up_date: date | None = None
    is_remote: bool | None = None
    tag_names: list[str] | None = None
    resume_id: int | None = None


class JobResponse(BaseModel):
    """Serialized job application."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    role: str
    status: str
    salary_min: int | None = None
    salary_max: int | None = None
    job_url: str | None = None
    notes: str | None = None
    application_date: date
    follow_up_date: date | None = None
    is_remote: bool
    created_at: datetime
    updated_at: datetime
    company: CompanySummary
    tags: list[TagSummary]
    resume: ResumeSummary | None = None


class DashboardStats(BaseModel):
    """Headline dashboard metrics."""

    total_applications: int
    interviews: int
    offers: int
    rejections: int
    active_followups: int


class MonthlyApplications(BaseModel):
    """Month-by-month application trend."""

    month: str
    count: int


class StatusDistributionItem(BaseModel):
    """Application count by status."""

    status: str
    count: int


class AnalyticsResponse(BaseModel):
    """Aggregated analytics payload."""

    monthly_applications: list[MonthlyApplications]
    status_distribution: list[StatusDistributionItem]
