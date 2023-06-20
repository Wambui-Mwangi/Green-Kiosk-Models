from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    orders_display = ('order_Number','order_Total', 'customer', 'date', 'products', 'payment_Options')

admin.site.register(Order,OrderAdmin)
