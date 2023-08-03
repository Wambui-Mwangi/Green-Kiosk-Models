from django import forms
from .models import Cart


class ProductCartForm(forms.ModelForm):
    class Meta: 
        model = Cart
        fields = "__all__"           #renders all attributes  