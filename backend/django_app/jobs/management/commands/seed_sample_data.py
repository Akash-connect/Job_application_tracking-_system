"""Seed the database with a demo user and sample applications."""

from datetime import date, timedelta

from django.core.management.base import BaseCommand

from accounts.models import User
from jobs.models import Company, JobApplication, Resume, Tag


class Command(BaseCommand):
    help = "Create sample JATS data for local development."

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username="demo",
            defaults={"email": "demo@example.com", "title": "Product Engineer"},
        )
        if created:
            user.set_password("demo12345")
            user.save()

        company_a, _ = Company.objects.get_or_create(owner=user, name="Nova Systems", defaults={"location": "Remote"})
        company_b, _ = Company.objects.get_or_create(owner=user, name="Blue Orbit", defaults={"location": "Bengaluru"})

        frontend, _ = Tag.objects.get_or_create(owner=user, name="Frontend", defaults={"color": "#38bdf8"})
        remote, _ = Tag.objects.get_or_create(owner=user, name="Remote", defaults={"color": "#34d399"})
        backend, _ = Tag.objects.get_or_create(owner=user, name="Backend", defaults={"color": "#f59e0b"})

        resume, _ = Resume.objects.get_or_create(
            owner=user,
            title="Senior Engineer Resume",
            defaults={"file": "resumes/demo-resume.pdf", "version": "v3"},
        )

        records = [
            {
                "company": company_a,
                "role": "Senior Frontend Engineer",
                "status": JobApplication.Status.INTERVIEW,
                "application_date": date.today() - timedelta(days=9),
                "follow_up_date": date.today() + timedelta(days=2),
                "is_remote": True,
                "salary_min": 1800000,
                "salary_max": 2400000,
                "notes": "Panel round scheduled next week.",
                "tags": [frontend, remote],
            },
            {
                "company": company_b,
                "role": "Platform Engineer",
                "status": JobApplication.Status.APPLIED,
                "application_date": date.today() - timedelta(days=4),
                "follow_up_date": date.today() + timedelta(days=5),
                "is_remote": False,
                "salary_min": 2200000,
                "salary_max": 2800000,
                "notes": "Reached out through referral channel.",
                "tags": [backend],
            },
        ]

        for payload in records:
            tags = payload.pop("tags")
            application, _ = JobApplication.objects.get_or_create(
                owner=user,
                company=payload["company"],
                role=payload["role"],
                defaults={**payload, "resume": resume},
            )
            application.tags.set(tags)

        self.stdout.write(self.style.SUCCESS("Sample data is ready. Demo credentials: demo / demo12345"))

