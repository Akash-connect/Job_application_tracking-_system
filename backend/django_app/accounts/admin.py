"""Admin configuration for user management."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Expose custom user fields in Django admin."""

    fieldsets = UserAdmin.fieldsets + (
        ("Preferences", {"fields": ("theme_preference", "title")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email", "theme_preference", "title")}),
    )
    list_display = ("username", "email", "title", "is_staff", "theme_preference")
    search_fields = ("username", "email", "title")

