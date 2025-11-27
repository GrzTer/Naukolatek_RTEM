from django.test import TestCase
from .models import EnergyConsumption
from datetime import datetime


class TestEnergyConsumptionModel(TestCase):
    def test_create_energy_consumption(self):
        EnergyConsumption.objects.create(
            device_id=1,
            timestamp=datetime.now(),
            energy_consumption=10.5,
        )
        self.assertEqual(EnergyConsumption.objects.count(), 1)
