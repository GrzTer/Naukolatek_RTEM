from django.shortcuts import render

from RTEM.MZE.models import Device


def Device_list(request):
    all_books = Device.serial_number.all()
    context = {
        'devices': all_books
    }
    return render(request, 'Device_list.html', context=context)
