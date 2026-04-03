"""Repository helpers for job application queries."""

from django.core.files.base import ContentFile
from django.db.models import Count, Q
from django.db.models.functions import TruncMonth

from jobs.models import Company, JobApplication, Resume, Tag


class JobRepository:
    """Encapsulate ORM access for job application resources."""

    @staticmethod
    def list_jobs_for_user(user_id: int, search: str | None = None, status: str | None = None, tag: str | None = None):
        queryset = JobApplication.objects.select_related("company", "resume").prefetch_related("tags").filter(owner_id=user_id)
        if search:
            queryset = queryset.filter(Q(role__icontains=search) | Q(company__name__icontains=search) | Q(notes__icontains=search))
        if status:
            queryset = queryset.filter(status=status)
        if tag:
            queryset = queryset.filter(tags__name__iexact=tag)
        return queryset.distinct()

    @staticmethod
    def get_job_for_user(user_id: int, job_id: int) -> JobApplication | None:
        return JobApplication.objects.select_related("company", "resume").prefetch_related("tags").filter(owner_id=user_id, id=job_id).first()

    @staticmethod
    def get_or_create_company(user_id: int, payload: dict) -> Company:
        company, _ = Company.objects.get_or_create(
            owner_id=user_id,
            name=payload["name"],
            defaults={
                "website": payload.get("website", "") or "",
                "location": payload.get("location", "") or "",
                "notes": payload.get("notes", "") or "",
            },
        )
        return company

    @staticmethod
    def get_resume_for_user(user_id: int, resume_id: int | None) -> Resume | None:
        if not resume_id:
            return None
        return Resume.objects.filter(owner_id=user_id, id=resume_id).first()

    @staticmethod
    def list_resumes_for_user(user_id: int):
        return Resume.objects.filter(owner_id=user_id).order_by("-created_at")

    @staticmethod
    def create_resume(user_id: int, title: str, version: str, file) -> Resume:
        content = ContentFile(file.file.read(), name=file.filename)
        return Resume.objects.create(owner_id=user_id, title=title, version=version, file=content)

    @staticmethod
    def get_or_create_tags(user_id: int, tag_names: list[str]) -> list[Tag]:
        tags = []
        for tag_name in tag_names:
            tag, _ = Tag.objects.get_or_create(owner_id=user_id, name=tag_name, defaults={"color": "#7dd3fc"})
            tags.append(tag)
        return tags

    @staticmethod
    def create_job(user_id: int, data: dict, company: Company, resume: Resume | None, tags: list[Tag]) -> JobApplication:
        job = JobApplication.objects.create(owner_id=user_id, company=company, resume=resume, **data)
        if tags:
            job.tags.set(tags)
        return job

    @staticmethod
    def delete_job(job: JobApplication) -> None:
        job.delete()

    @staticmethod
    def dashboard_stats(user_id: int) -> dict:
        queryset = JobApplication.objects.filter(owner_id=user_id)
        return {
            "total_applications": queryset.count(),
            "interviews": queryset.filter(status=JobApplication.Status.INTERVIEW).count(),
            "offers": queryset.filter(status=JobApplication.Status.OFFER).count(),
            "rejections": queryset.filter(status=JobApplication.Status.REJECTED).count(),
            "active_followups": queryset.filter(follow_up_date__isnull=False).count(),
        }

    @staticmethod
    def monthly_applications(user_id: int):
        return (
            JobApplication.objects.filter(owner_id=user_id)
            .annotate(month=TruncMonth("application_date"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )

    @staticmethod
    def status_distribution(user_id: int):
        return (
            JobApplication.objects.filter(owner_id=user_id)
            .values("status")
            .annotate(count=Count("id"))
            .order_by("status")
        )
