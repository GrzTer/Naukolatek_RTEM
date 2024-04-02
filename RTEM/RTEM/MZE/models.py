# # mze/models.py
# from django.db import models
# from django.utils.timezone import now
# import uuid
#
#
# # def generate_serial_number():
# #     timestamp = now().strftime('%Y%m%d%H%M%S')
# #     unique_id = uuid.uuid4().hex[:6]
# #     return f"{timestamp}-{unique_id}"
#
#
# class Device(models.Model):
#     serial_number = models.CharField(max_length=100, unique=True, default=generate_serial_number)
#     type = models.CharField(max_length=100)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return f"{self.type} - {self.serial_number}"
#
#
# class SensorData(models.Model):
#     device = models.ForeignKey(Device, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField()
#     energy_usage = models.FloatField()  # Zużycie energii w kWh
#
#     def __str__(self):
#         return f"{self.device.serial_number} - {self.timestamp} - {self.energy_usage}"
