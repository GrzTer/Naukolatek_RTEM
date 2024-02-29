from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Sensor(models.Model):
    identifier = models.CharField(max_length=100, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='sensors')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.identifier


class Device(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='devices')
    sensors = models.ManyToManyField(Sensor, related_name='devices')

    def __str__(self):
        return self.name


class EnergyConsumptionRecord(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='consumption_records')
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_consumed = models.FloatField()  # wartość w kWh
    frequency = models.FloatField(null=True, blank=True, help_text="Frequency in Hz")  # Częstotliwość w Hz, może być null
    resistance = models.FloatField(null=True, blank=True, help_text="Resistance in Ohms")  # Rezystancja w Omach, może być null
    voltage = models.FloatField(null=True, blank=True, help_text="Voltage in Volts")  # Napięcie w Voltach, może być null
    temperature = models.FloatField(null=True, blank=True, help_text="Temperature in Celsius")  # Temperatura w stopniach Celsjusza, może być null

    def __str__(self):
        return f"{self.sensor.identifier} - {self.timestamp} - {self.energy_consumed}kWh"