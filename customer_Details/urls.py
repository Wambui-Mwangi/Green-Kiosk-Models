from django.urls import path
from .views import register_customer, customer_detail, edit_customer

urlpatterns = [
    path("customers/register/", register_customer, name="customer_register_view"),
    path('customers/details/<int:id>/', customer_detail, name='customer_details_view'),
    path("customers/edit/<int:id>/", edit_customer, name='customer_edit_view')

]