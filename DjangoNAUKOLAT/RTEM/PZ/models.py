from django.db import models


class EnergyForecast(models.Model):
    date = models.DateField()
    predicted_consumption = models.FloatField()

    def __str__(self):
        return f"Forecast for {self.date}: Predicted - {self.predicted_consumption} kWh"
