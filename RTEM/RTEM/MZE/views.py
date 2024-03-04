from django.http import JsonResponse
from .models import Device, SensorData
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime


@csrf_exempt
def collect_sensor_data(request):
    if request.method == 'POST':
        device_serial = request.POST.get('serial_number')
        timestamp = parse_datetime(request.POST.get('timestamp'))
        energy_usage = request.POST.get('energy_usage')

        device, created = Device.objects.get_or_create(serial_number=device_serial)

        SensorData.objects.create(
            device=device,
            timestamp=timestamp,
            energy_usage=energy_usage
        )

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)
