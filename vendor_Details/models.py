from django.db import models

# Create your models here.
class Vendor(models.Model):
    store_name = models.CharField(max_length=50)
    vendor_Name = models.CharField(max_length=32, default="")
    location = models.CharField(max_length=50)
    password = models.CharField(max_length=18)
    contact = models.PositiveIntegerField()

    def __str__(self):
        return self.store_name
