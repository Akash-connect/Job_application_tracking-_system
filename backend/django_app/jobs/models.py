"""Domain models for companies, resumes, tags, and job applications."""

from django.conf import settings
from django.db import models


class TimeStampedModel(models.Model):
    """Abstract base model with audit timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Company(TimeStampedModel):
    """A company tied to one or more job applications."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="companies")
    name = models.CharField(max_length=180)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=180, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ("owner", "name")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Tag(TimeStampedModel):
    """Free-form categorization tags for applications."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tags")
    name = models.CharField(max_length=80)
    color = models.CharField(max_length=7, default="#7dd3fc")

    class Meta:
        unique_together = ("owner", "name")
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Resume(TimeStampedModel):
    """Uploaded resume assets tied to a user."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="resumes")
    title = models.CharField(max_length=120)
    file = models.FileField(upload_to="resumes/")
    version = models.CharField(max_length=40, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class JobApplication(TimeStampedModel):
    """A job application tracked across its lifecycle."""

    class Status(models.TextChoices):
        APPLIED = "applied", "Applied"
        INTERVIEW = "interview", "Interview"
        OFFER = "offer", "Offer"
        REJECTED = "rejected", "Rejected"

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="applications")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="applications")
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True, related_name="applications")
    role = models.CharField(max_length=180)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.APPLIED)
    salary_min = models.PositiveIntegerField(null=True, blank=True)
    salary_max = models.PositiveIntegerField(null=True, blank=True)
    job_url = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    application_date = models.DateField()
    follow_up_date = models.DateField(null=True, blank=True)
    is_remote = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="applications")

    class Meta:
        ordering = ["-application_date", "-updated_at"]

    def __str__(self) -> str:
        return f"{self.role} @ {self.company.name}"

