from django.db import models

# Create your models here.
class AddVehicle(models.Model):

    vehicle_number = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    company = models.TextField(max_length=9)

    def __str__(self):
        return self.vehicle_number
