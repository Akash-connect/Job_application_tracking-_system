"""Admin configuration for job-tracking models."""

from django.contrib import admin

from .models import Company, JobApplication, Resume, Tag


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Admin list for companies."""

    list_display = ("name", "owner", "location", "website", "created_at")
    search_fields = ("name", "location", "owner__username")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Admin list for tags."""

    list_display = ("name", "owner", "color", "created_at")
    search_fields = ("name", "owner__username")


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    """Admin list for resumes."""

    list_display = ("title", "owner", "version", "created_at")
    search_fields = ("title", "owner__username")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    """Admin list for job applications."""

    list_display = ("role", "company", "owner", "status", "application_date", "follow_up_date", "is_remote")
    list_filter = ("status", "is_remote", "application_date")
    search_fields = ("role", "company__name", "owner__username", "notes")
    autocomplete_fields = ("company", "resume", "tags")

