"""Initial jobs schema."""

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=180)),
                ("website", models.URLField(blank=True)),
                ("location", models.CharField(blank=True, max_length=180)),
                ("notes", models.TextField(blank=True)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="companies", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["name"], "unique_together": {("owner", "name")}},
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=120)),
                ("file", models.FileField(upload_to="resumes/")),
                ("version", models.CharField(blank=True, max_length=40)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="resumes", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=80)),
                ("color", models.CharField(default="#7dd3fc", max_length=7)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="tags", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["name"], "unique_together": {("owner", "name")}},
        ),
        migrations.CreateModel(
            name="JobApplication",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("role", models.CharField(max_length=180)),
                ("status", models.CharField(choices=[("applied", "Applied"), ("interview", "Interview"), ("offer", "Offer"), ("rejected", "Rejected")], default="applied", max_length=20)),
                ("salary_min", models.PositiveIntegerField(blank=True, null=True)),
                ("salary_max", models.PositiveIntegerField(blank=True, null=True)),
                ("job_url", models.URLField(blank=True)),
                ("notes", models.TextField(blank=True)),
                ("application_date", models.DateField()),
                ("follow_up_date", models.DateField(blank=True, null=True)),
                ("is_remote", models.BooleanField(default=False)),
                ("company", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="applications", to="jobs.company")),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="applications", to=settings.AUTH_USER_MODEL)),
                ("resume", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="applications", to="jobs.resume")),
                ("tags", models.ManyToManyField(blank=True, related_name="applications", to="jobs.tag")),
            ],
            options={"ordering": ["-application_date", "-updated_at"]},
        ),
    ]
