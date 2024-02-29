from django.contrib import admin
from .models import Device, EnergyConsumptionRecord, Location, Sensor
admin.site.register(Sensor)
admin.site.register(Location)
admin.site.register(Device)
admin.site.register(EnergyConsumptionRecord)
