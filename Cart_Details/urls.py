from django.urls import path
from .import views
from .views import product_cart


urlpatterns = [
    # path("product_cart/", product_cart, name="product_cart_view"),
    path("product_cart/<int:product_id>/", views.product_cart, name='product_cart')

]