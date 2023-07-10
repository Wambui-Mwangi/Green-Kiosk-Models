from django.contrib import admin
from .models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'total', 'number_of_products', 'shipping_cost', 'payment_options', 'discount')

admin.site.register(Cart, CartAdmin) 