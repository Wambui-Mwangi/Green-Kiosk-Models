from django.contrib import admin
from .models import Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_Number','order_Total', 'customer', 'date', 'products', 'payment_Options')

admin.site.register(Order,OrderAdmin)
