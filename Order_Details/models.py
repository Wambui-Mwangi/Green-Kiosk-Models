from django.db import models
from Payment_Details.models import Payment
from Cart_Details.models import Cart
from Delivery.models import Shipment
from customer_Details.models import Customers

# Create your models here.
class Order(models.Model):
    payment = models.OneToOneField(Payment, models.PROTECT, null=True,related_name='orders')
    basket = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipment = models.ForeignKey(Shipment, related_name='related_shipment', on_delete=models.CASCADE)

    # shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    custom = models.ManyToManyField(Customers)
    customer = models.CharField(max_length=50)
    order_Number = models.IntegerField()
    order_Total = models.FloatField()
    date = models.DateTimeField()
    products = models.TextField()
    payment_Options = models.CharField(max_length=20)

    def __str__(self):
        return self.customer
    