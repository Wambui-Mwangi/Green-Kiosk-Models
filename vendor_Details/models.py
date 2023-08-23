from django.db import models

# Create your models here.
class Vendor(models.Model):
    store_name = models.CharField(max_length=50)
    vendor_Name = models.CharField(max_length=32, default="")
    image = models.ImageField(upload_to= 'images/')
    location = models.CharField(max_length=50)
    password = models.CharField(max_length=18)
    email = models.CharField(max_length=32)
    contact = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
