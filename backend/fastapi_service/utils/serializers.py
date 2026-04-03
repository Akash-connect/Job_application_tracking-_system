"""Serialization helpers for Django ORM objects exposed via FastAPI."""


def serialize_resume(resume):
    """Convert a Resume model instance into a plain dictionary."""
    return {
        "id": resume.id,
        "title": resume.title,
        "version": resume.version,
        "file": resume.file.url if getattr(resume.file, "url", None) else str(resume.file),
    }


def serialize_job(job):
    """Convert a JobApplication model instance into a plain dictionary."""
    return {
        "id": job.id,
        "role": job.role,
        "status": job.status,
        "salary_min": job.salary_min,
        "salary_max": job.salary_max,
        "job_url": job.job_url,
        "notes": job.notes,
        "application_date": job.application_date,
        "follow_up_date": job.follow_up_date,
        "is_remote": job.is_remote,
        "created_at": job.created_at,
        "updated_at": job.updated_at,
        "company": {
            "id": job.company.id,
            "name": job.company.name,
            "website": job.company.website,
            "location": job.company.location,
            "notes": job.company.notes,
        },
        "tags": [
            {
                "id": tag.id,
                "name": tag.name,
                "color": tag.color,
            }
            for tag in job.tags.all()
        ],
        "resume": serialize_resume(job.resume) if job.resume else None,
    }
