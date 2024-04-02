from django.shortcuts import render

from MZE.models import Device


def Device_list(request):
    all_devices = Device.serial_number
    context = {
        'devices': all_devices
    }
    return render(request, 'Device_list.html', context=context)
