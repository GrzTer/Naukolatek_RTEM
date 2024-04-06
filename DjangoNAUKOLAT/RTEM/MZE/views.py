from django.shortcuts import render
from .models import EnergyConsumption
import json
from django.core.serializers.json import DjangoJSONEncoder

def chart_view(request):
    # Query your model for the data
    queryset = EnergyConsumption.objects.all().order_by('timestamp')
    data = list(queryset.values('timestamp', 'energy_consumption'))

    # Convert data to JSON format
    chart_data = json.dumps(data, cls=DjangoJSONEncoder)

    return render(request, 'MZE.html', {'chart_data': chart_data})
