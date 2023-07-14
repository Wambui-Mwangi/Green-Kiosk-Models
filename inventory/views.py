from django.shortcuts import render
from .forms import ProductUploadForm

#there are class based views and function based views

# Create your views here.
def upload_product(request):                      #the request represents a http request
    form = ProductUploadForm()
    return render(request, "inventory/product_upload.html", {"form": form})