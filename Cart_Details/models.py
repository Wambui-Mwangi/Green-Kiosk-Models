from django.db import models
from inventory.models import Product
from customer_Details.models import User
# from Order_Details.models import Order

# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=32)
    products = models.ManyToManyField(Product)
    total = models.PositiveIntegerField(default=0)
    number_of_products = models.PositiveIntegerField(null=True, blank=True)
    shipping_cost = models.FloatField(null=True, blank=True)
    payment_options = models.CharField(max_length=20)
    discount = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return self.product
    