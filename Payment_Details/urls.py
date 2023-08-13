from django.urls import path
from .views import choose_payment


urlpatterns = [
    path("payment/<int:order_id>/", choose_payment, name="payment_process_view"),
]