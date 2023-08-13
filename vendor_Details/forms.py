from django import forms
from django.contrib.auth.forms import UserCreationForm
from vendor_Details.models import Vendor

class VendorUploadForm(forms.ModelForm):
    class Meta: 
        model = Vendor
        fields = "__all__"           #renders all attributes  

