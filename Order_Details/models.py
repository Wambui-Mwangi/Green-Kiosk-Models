from django.db import models

# Create your models here.
class Order(models.Model):
    customer = models.CharField(max_length=50)
    order_Number = models.IntegerField()
    order_Total = models.FloatField()
    date = models.DateTimeField()
    products = models.TextField()
    payment_Options = models.CharField(max_length=20)

    def __str__(self):
        return self.customer