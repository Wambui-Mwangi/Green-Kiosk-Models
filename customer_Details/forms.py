from django import forms
from django.contrib.auth.forms import UserCreationForm
from customer_Details.models import Customers

class CustomerUploadForm(forms.ModelForm):
    class Meta: 
        model = Customers
        fields = "__all__"           #renders all attributes  

