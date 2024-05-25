from django.contrib import admin

# Register your models here.
from .models import Product, ProductSubCat

admin.site.register(Product)
admin.site.register(ProductSubCat)

