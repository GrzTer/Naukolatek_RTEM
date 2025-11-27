from django.db import models


# Each model maps to a single database table.
# The EnergyConsumption model will have a corresponding table in the database
# that stores energy consumption data for various devices.
class EnergyConsumption(models.Model):
    # Define fields for the model. Each field corresponds to a database column.
    device_id = models.IntegerField()
    timestamp = models.DateTimeField()
    energy_consumption = models.FloatField()

    # This method returns a human-readable string representation of the object.
    # It's useful for debugging and in the Django admin.
    def __str__(self):
        # Customize the string representation of EnergyConsumption instances
        return (
            f"Device {self.device_id} at {self.timestamp} - "
            f"{self.energy_consumption} kWh"
        )

    # Meta options - used to define metadata for your model
    class Meta:
        # Human-readable name for the model in the admin
        verbose_name = "Energy Consumption"
        # Human-readable plural name for the model in the admin
        verbose_name_plural = "Energy Consumptions"
        # Optional: Ordering of the records when querying the database
        # Records are ordered by timestamp in descending order
        ordering = ["-timestamp"]
