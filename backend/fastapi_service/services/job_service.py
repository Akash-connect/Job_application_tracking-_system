"""Business logic for job application and analytics operations."""

from fastapi import HTTPException, status

from jobs.models import JobApplication

from ..repositories.job_repository import JobRepository


class JobService:
    """Coordinate job CRUD, kanban updates, and analytics."""

    def list_jobs(self, user_id: int, search: str | None, status_filter: str | None, tag: str | None):
        return JobRepository.list_jobs_for_user(user_id=user_id, search=search, status=status_filter, tag=tag)

    def create_job(self, user_id: int, payload: dict) -> JobApplication:
        company = JobRepository.get_or_create_company(user_id=user_id, payload=payload.pop("company"))
        resume = JobRepository.get_resume_for_user(user_id=user_id, resume_id=payload.pop("resume_id", None))
        tags = JobRepository.get_or_create_tags(user_id=user_id, tag_names=payload.pop("tag_names", []))
        return JobRepository.create_job(user_id=user_id, data=payload, company=company, resume=resume, tags=tags)

    def update_job(self, user_id: int, job_id: int, payload: dict) -> JobApplication:
        job = JobRepository.get_job_for_user(user_id=user_id, job_id=job_id)
        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job application not found")

        company_payload = payload.pop("company", None)
        tag_names = payload.pop("tag_names", None)
        resume_id = payload.pop("resume_id", None) if "resume_id" in payload else None

        if company_payload:
            job.company = JobRepository.get_or_create_company(user_id=user_id, payload=company_payload)

        for field, value in payload.items():
            if value is not None:
                setattr(job, field, value)

        if resume_id is not None:
            job.resume = JobRepository.get_resume_for_user(user_id=user_id, resume_id=resume_id)

        job.save()

        if tag_names is not None:
            tags = JobRepository.get_or_create_tags(user_id=user_id, tag_names=tag_names)
            job.tags.set(tags)

        refreshed = JobRepository.get_job_for_user(user_id=user_id, job_id=job_id)
        if not refreshed:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job application not found after update")
        return refreshed

    def delete_job(self, user_id: int, job_id: int) -> None:
        job = JobRepository.get_job_for_user(user_id=user_id, job_id=job_id)
        if not job:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Job application not found")
        JobRepository.delete_job(job)

    def analytics(self, user_id: int) -> dict:
        monthly = [
            {"month": item["month"].strftime("%b %Y"), "count": item["count"]}
            for item in JobRepository.monthly_applications(user_id=user_id)
            if item["month"]
        ]
        distribution = [
            {"status": item["status"], "count": item["count"]}
            for item in JobRepository.status_distribution(user_id=user_id)
        ]
        return {"monthly_applications": monthly, "status_distribution": distribution}

    def dashboard_stats(self, user_id: int) -> dict:
        return JobRepository.dashboard_stats(user_id=user_id)

    def list_resumes(self, user_id: int):
        return JobRepository.list_resumes_for_user(user_id=user_id)

    def upload_resume(self, user_id: int, title: str, version: str, file):
        return JobRepository.create_resume(user_id=user_id, title=title, version=version, file=file)
