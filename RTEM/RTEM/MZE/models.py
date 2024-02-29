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

    def __str__(self):
        return f"{self.sensor.identifier} - {self.timestamp} - {self.energy_consumed}kWh"
