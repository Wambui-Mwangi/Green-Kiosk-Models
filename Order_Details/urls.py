from django.urls import path
from .views import orders_list


urlpatterns = [
    path("orders/<int:order_id>/", orders_list, name="orders_list_view"),
]