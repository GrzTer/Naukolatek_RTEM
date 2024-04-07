# energyforecast/views.py
from django.shortcuts import render
from .forecasting import forecast_energy_consumption

def forecast_view(request):
    forecasted_value = forecast_energy_consumption()
    return render(request, 'energyforecast/forecast.html', {'forecasted_value': forecasted_value})
