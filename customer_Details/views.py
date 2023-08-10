from django.shortcuts import render, redirect
from .forms import CustomerUploadForm
from customer_Details.models import Customers

# Create your views here.
def register_customer(request):                   
    if request.method == 'POST':
        uploaded_customer = request.FILES["image"]
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomerUploadForm()

    return render(request, "customer_Details/customer_upload.html", {"form": form})

def customer_detail(request, id):
    customer = Customers.objects.get(id=id)
    return render (request, "customer_Details/customer_details.html", {"customer": customer})

def edit_customer(request, id):
    product = Customers.objects.get(id = id)
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('customer_details_view', id=product.id)

    else:
        form=CustomerUploadForm(instance=product)
        return render (request, 'customer_Details/edit_customer.html', {"form":form}) 