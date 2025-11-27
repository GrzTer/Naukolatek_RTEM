import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RTEM.settings")
django.setup()

User = get_user_model()

if __name__ == "__main__":
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin")
        print("Superuser created.")
    else:
        print("Superuser already exists.")
