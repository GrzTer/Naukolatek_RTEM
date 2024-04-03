from django.contrib import admin
from .models import EnergyConsumption

@admin.register(EnergyConsumption)
class EnergyConsumptionAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'timestamp', 'energy_consumption')
    list_filter = ('device_id',)
