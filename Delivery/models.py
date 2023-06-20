from django.db import models

# Create your models here.
class Shipment(models.Model):
    location = models.CharField(max_length=200)
    order = models.TextField()
    date = models.DateTimeField()
    type_of_delivery = models.BooleanField()
    shipment_cost = models.FloatField()
    status = models.TextField()
    delivery_time = models.TimeField()

    def __str_(self):
        return self.location
