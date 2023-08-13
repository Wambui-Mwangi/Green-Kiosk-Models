from django.urls import path
from .views import register_vendor, vendor_details, edit_vendor

urlpatterns = [
    path("vendors/register/", register_vendor, name="vendor_register_view"),
    path('vendors/details/<int:id>/', vendor_details, name='vendor_details_view'),
    path("vendors/edit/<int:id>/", edit_vendor, name='vendor_edit_view')
]