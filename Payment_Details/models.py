from django.db import models


# Create your models here.
class Payment(models.Model):
    receipt = models.TextField()
    amount = models.FloatField()
    payment_option = models.CharField(max_length=20)
    date = models.DateTimeField()
    status = models.CharField(max_length=20)
    order = models.TextField()

    def __str__(self):
        return self.receipt