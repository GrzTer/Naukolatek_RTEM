from django.db import models


class EnergyConsumption(models.Model):
    device_id = models.IntegerField()
    timestamp = models.DateTimeField()
    energy_consumption = models.FloatField()

    def __str__(self):
        return f"Device {self.device_id} at {self.timestamp} - {self.energy_consumption} kWh"

    class Meta:
        verbose_name = "Energy Consumption"
        verbose_name_plural = "Energy Consumptions"
        ordering = ["-timestamp"]
