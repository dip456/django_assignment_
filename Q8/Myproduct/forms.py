from django import forms
from .models import Product, ProductSubCat

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name']

class ProductSubCatForm(forms.ModelForm):
    class Meta:
        model = ProductSubCat
        fields = ['product', 'price', 'image', 'model', 'ram']
