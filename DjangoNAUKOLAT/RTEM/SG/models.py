from django.db import models

class EnergyPrice(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    country_code = models.CharField(max_length=2)  # Przykładowy kod kraju (np. 'PL', 'US')
