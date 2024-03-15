from django.contrib import admin
from .models import Device, TemperatureMeasurement, VoltageMeasurement
admin.site.register(Device)
admin.site.register(TemperatureMeasurement)
admin.site.register(VoltageMeasurement)