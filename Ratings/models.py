from django.db import models
from customer_Details.models import Customers
from inventory.models import Product

# Create your models here.
class Reviews(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return self.sender

    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'