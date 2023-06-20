from django.contrib import admin
from .models import Customers


# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    display = ('first_Name', 'last_Name', 'phone_Number', 'email', 'address', 'date_created', 'date_updated')

admin.site.register(Customers, CustomerAdmin)

