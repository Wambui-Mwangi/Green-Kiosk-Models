from django.contrib import admin

from .models import Product      #.models means the model is in the surrent directory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", 'stock', 'price', 'date_created')  #they have to be attributes of the product class. this is a tuple

admin.site.register(Product, ProductAdmin)
