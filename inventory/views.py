from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product
from Ratings.models import Reviews
from django.shortcuts import redirect

#there are class based views and function based views

# Create your views here.
def upload_product(request):                      #the request represents a http request
    if request.method == 'POST':
        uploaded_product = request.FILES["image"]
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            product=form.save()
            return redirect('product_detail_view', id=product.id)
    else:
        form = ProductUploadForm()

    return render(request, "inventory/product_upload.html", {"form": form})
    

def products_list(request):
    products = Product.objects.all()
    product_ratings = {}
    for product in products:
        ratings = Reviews.objects.filter(product=product)
        product_ratings[product.id] = ratings

    context = {
        'products':products,
        'product_ratings': product_ratings
    }

    return render (request, "inventory/products_list.html", context)

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render (request, "inventory/product_details.html", {"product": product})

def edit_product_view(request, id):
    product = Product.objects.get(id = id)
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view', id=product.id)

    else:
        form=ProductUploadForm(instance=product)
        return render (request, 'inventory/edit_product.html', {"form":form})    