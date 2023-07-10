from django.contrib import admin
from .models import Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('sender', 'message', 'product', 'number_of_stars', 'date')

admin.site.register(Reviews,ReviewsAdmin)
