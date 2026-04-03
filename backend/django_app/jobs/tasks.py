"""Celery tasks for background reminders."""

from celery import shared_task
from django.utils import timezone

from .models import JobApplication


@shared_task
def collect_due_followups() -> list[dict]:
    """Collect applications needing follow-up notifications."""
    today = timezone.now().date()
    applications = JobApplication.objects.select_related("company", "owner").filter(follow_up_date__lte=today)
    return [
        {
            "application_id": application.id,
            "email": application.owner.email,
            "company": application.company.name,
            "role": application.role,
            "follow_up_date": application.follow_up_date.isoformat() if application.follow_up_date else None,
        }
        for application in applications
    ]
