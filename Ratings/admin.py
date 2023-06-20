from django.contrib import admin
from .models import Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    reviews_display = ('sender', 'message', 'product', 'number_of_starts', 'date')

admin.site.register(Reviews,ReviewsAdmin)
