from django.db import models
from MZE.models import Device

class ConsumptionRecord(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    energy_consumed = models.FloatField()  # kWh

class OptimizationSuggestion(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    suggestion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)