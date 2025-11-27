from django.test import TestCase
from .models import EnergyConsumption
from django.utils import timezone

class EnergyConsumptionModelTest(TestCase):
    def test_energy_consumption_str(self):
        """
        Test the __str__ method of the EnergyConsumption model.
        """
        timestamp = timezone.now()
        energy_consumption = EnergyConsumption.objects.create(
            device_id=1,
            timestamp=timestamp,
            energy_consumption=10.5
        )
        self.assertEqual(
            str(energy_consumption),
            f"Device 1 at {timestamp} - 10.5 kWh"
        )
