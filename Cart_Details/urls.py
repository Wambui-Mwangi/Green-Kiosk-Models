from django.urls import path
from .views import product_cart


urlpatterns = [
    path("product_cart/", product_cart, name="product_cart_view"),

]