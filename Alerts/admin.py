from django.contrib import admin
from .models import Notifications

# Register your models here.
class NotificationsAdmin(admin.ModelAdmin):
    display_notifications = ('message', 'date', 'customer')

admin.site.register(Notifications, NotificationsAdmin)
