from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product

#there are class based views and function based views

# Create your views here.
def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ProductUploadForm()

    return render(request, "inventory/product_upload.html", {"form": form})


def products_list(request):
    products = Product.objects.all()
    return render (request, "inventory/products_list.html", {"products": products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, "inventory/product_details.html", {"product": product})