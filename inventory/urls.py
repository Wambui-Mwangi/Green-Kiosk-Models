from django.urls import path
from .views import upload_product, products_list, product_detail


urlpatterns = [
    path("products/upload", upload_product, name="product_upload_view"),
    path("products/list", products_list, name = "products_list_view"),
    path("products/<int:id>/", product_detail, name= "product_detail_view")
]