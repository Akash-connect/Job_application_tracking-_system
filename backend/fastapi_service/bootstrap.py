"""Bootstrap Django ORM usage inside FastAPI."""

from pathlib import Path
import os
import sys


BASE_DIR = Path(__file__).resolve().parents[1]
DJANGO_DIR = BASE_DIR / "django_app"

if str(DJANGO_DIR) not in sys.path:
    sys.path.insert(0, str(DJANGO_DIR))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django  # noqa: E402

django.setup()

