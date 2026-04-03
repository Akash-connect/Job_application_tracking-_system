"""Custom user model for the JATS project."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Application user extended with profile preferences."""

    email = models.EmailField(unique=True)
    theme_preference = models.CharField(max_length=10, default="dark")
    title = models.CharField(max_length=120, blank=True)

    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username

