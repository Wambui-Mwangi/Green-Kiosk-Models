from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_Name', 'location', 'store_name', 'password', 'contact', 'image')

admin.site.register(Vendor, VendorAdmin)