from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from .models import EnergyConsumption
import json


def chart_view(request):
    data = EnergyConsumption.objects.order_by("timestamp").values(
        "timestamp", "energy_consumption", "device_id"
    )
    formatted_data = [
        {
            "timestamp": item["timestamp"].isoformat(),
            "energy_consumption": format(float(item["energy_consumption"]), ".3f"),
            "device_id": item["device_id"],
        }
        for item in data
    ]
    chart_data = json.dumps(formatted_data, cls=DjangoJSONEncoder)
    return render(request, "MZE.html", {"chart_data": chart_data})
