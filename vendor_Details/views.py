from django.shortcuts import render, redirect
from .forms import VendorUploadForm
from vendor_Details.models import Vendor

# Create your views here.
def register_vendor(request):                   
    if request.method == 'POST':
        uploaded_vendor = request.FILES["image"]
        form = VendorUploadForm(request.POST, request.FILES)
        if form.is_valid():
            vendor=form.save()
            return redirect('vendor_detail_view', id=vendor.id)
    else:
        form = VendorUploadForm()

    return render(request, "vendor_Details/vendor_upload.html", {"form": form})

def vendor_details(request, id):
    vendor = Vendor.objects.get(id=id)
    return render (request, "vendor_Details/vendor_details.html", {"vendor": vendor})

def edit_vendor(request, id):
    product = Vendor.objects.get(id = id)
    if request.method == 'POST':
        form = VendorUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('vendor_details_view', id=product.id)

    else:
        form=VendorUploadForm(instance=product)
        return render (request, 'vendor_Details/edit_vendor.html', {"form":form}) 
   
   