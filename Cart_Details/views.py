from django.shortcuts import render
from .forms import ProductCartForm
from Cart_Details.models import Product


# Create your views here.
# def product_cart(request):                      #the request represents a http request
#     if request.method == 'POST':
#         uploaded_product = request.FILES["image"]
#         form = ProductCartForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ProductCartForm()

#     return render(request, "Cart_Details/product_cart.html", {"form": form})

def product_cart(request):
    products = Product.objects.all()
    return render (request, "Cart_Details/product_cart.html", {"products": products})
