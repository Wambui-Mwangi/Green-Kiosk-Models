from django.db import models

# Create your models here.
class Notifications(models.Model):
    message = models.TextField()
    date = models.DateTimeField()
    customer = models.CharField(max_length=50)

    def __str__(self):
        return self.message
    
    class Meta:
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'