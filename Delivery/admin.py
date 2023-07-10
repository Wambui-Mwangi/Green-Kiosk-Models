from django.contrib import admin
from .models import Shipment

# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('location', 'order', 'date', 'type_of_delivery', 'shipment_cost', 'status', 'delivery_time')

admin.site.register(Shipment,ShipmentAdmin)
