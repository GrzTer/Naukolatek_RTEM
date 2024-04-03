import os
import django
import pandas as pd
from django.core.management.base import BaseCommand

# Set up the Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RTEM.settings')
django.setup()

# Now you can safely import your models
from MZE.models import EnergyConsumption

class Command(BaseCommand):
    help = 'Import data from CSV to database'

    def handle(self, *args, **options):
        df = pd.read_csv('../../data1.csv')
        for _, row in df.iterrows():
            EnergyConsumption.objects.create(
                device_id=row['device_id'],
                timestamp=pd.to_datetime(row['timestamp']),
                energy_consumption=row['energy_consumption']
            )
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
