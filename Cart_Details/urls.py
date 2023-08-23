from django.urls import path
from .import views
from .views import product_cart, cart_contents, remove_from_cart


urlpatterns = [
    path("product_cart/", product_cart, name="product_cart_view"),
    path("product_cart/<int:product_id>/", product_cart, name='product_cart'),
    path("cart_contents/", cart_contents, name="cart_contents_view"),
    path("remove_cart/<int:product_id>", remove_from_cart , name='remove_from_cart_view')
]