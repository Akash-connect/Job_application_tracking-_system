"""Django project package and Celery loader."""

from .celery import app as celery_app

__all__ = ("celery_app",)
