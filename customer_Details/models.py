from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customers(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
    first_Name = models.CharField(max_length=32)
    last_Name = models.CharField(max_length=32)
    phone_Number = models.PositiveIntegerField()
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.first_Name} {self.last_Name}'
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'