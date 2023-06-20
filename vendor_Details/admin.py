from django.contrib import admin
from .models import Vendor

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    vendors_display = ('vendor_Name', 'location', 'store_name', 'password', 'contact')

admin.site.register(Vendor, VendorAdmin)