# oz/models.py
from django.db import models
# from MZE.models import Device # JAK TO POBRAĆ?


class OptimizationSuggestion(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    suggestion_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.serial_number} - {self.suggestion_text[:50]}"
