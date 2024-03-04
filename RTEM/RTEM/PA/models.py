# pa/models.py
from django.db import models
# from ..MZE.models import Device # JAK TO POBRAĆ?


class Alert(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device.serial_number} - {self.alert_type} - {self.timestamp}"
