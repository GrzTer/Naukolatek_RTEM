from django.db import models
import uuid


def generate_default_serial_number():
    return uuid.uuid4().hex  # Generuje unikalny identyfikator


class Device(models.Model):
    serial_number = models.CharField(max_length=100, unique=True, default=generate_default_serial_number)
    type = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.serial_number}"



class TemperatureMeasurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='temperature_measurements')
    temperature = models.FloatField()
    measurement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temperature {self.temperature}°C for {self.device.serial_number} on {self.measurement_date}"


class VoltageMeasurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='voltage_measurements')
    voltage = models.FloatField()
    measurement_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voltage {self.voltage}V for {self.device.serial_number} on {self.measurement_date}"
