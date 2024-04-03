from django.shortcuts import render
from .models import EnergyConsumption
import pandas as pd

def chart_view(request):
    # Load CSV file
    data = EnergyConsumption.objects.all().values('device_id', 'timestamp', 'energy_consumption')
    df = pd.DataFrame(data)

    # Convert 'timestamp' to more chart-friendly format if necessary
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d %H:%M')

    # Group data by 'device_id'
    grouped = df.groupby('device_id')

    series = []
    for device_id, group in grouped:
        series.append({
            'name': f'Device {device_id}',
            'data': group[['timestamp', 'energy_consumption']].values.tolist(),
        })

    # Convert data to JSON format for ApexCharts
    chart_data = {
        'series': series,
    }

    return render(request, 'MZE.html', {'chart_data': chart_data})
