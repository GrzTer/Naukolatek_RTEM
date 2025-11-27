import os
import django
from django.core.management import call_command

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RTEM.settings")
django.setup()

if __name__ == "__main__":
    call_command("makemigrations")
    call_command("migrate")
