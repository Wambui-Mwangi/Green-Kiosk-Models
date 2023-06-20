from django.db import models

# Create your models here.
class Reviews(models.Model):
    sender = models.CharField(max_length=40)
    message = models.TextField()
    product = models.CharField(max_length=40)
    number_of_stars = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.sender
