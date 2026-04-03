"""App configuration for job tracking."""

from django.apps import AppConfig


class JobsConfig(AppConfig):
    """Register the jobs application."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "jobs"

