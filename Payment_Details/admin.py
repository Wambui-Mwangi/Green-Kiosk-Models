from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    payments_Display = ('receipt', 'amount', 'payment_option', 'date', 'status', 'order')

admin.site.register(Payment, PaymentAdmin)

