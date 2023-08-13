from django.urls import path
from .import views
from .views import product_cart, cart_contents


urlpatterns = [
    path("product_cart/", product_cart, name="product_cart_view"),
    path("product_cart/<int:product_id>/", views.product_cart, name='product_cart'),
    path("cart_contents/", views.cart_contents, name="cart_contents_view")
]