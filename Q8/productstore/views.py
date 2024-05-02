from django.shortcuts import render,redirect

from .forms import ProductForm
from .models import ProductModel

# Create your views here.

def index_page_view(request):
    if request.method == 'POST':
        productName = request.POST['product_name']

        new_product = ProductModel(product_name = productName )
        new_product.save()
    
        
    context = {
        'form' : ProductForm(),
        'products' : ProductModel.objects.all()

    }

    return render(request,'productstore/index.html',context)

def delete_page(request,product_id):
    get_prod = ProductModel.objects.get(id=product_id)
    get_prod.delete()

    return redirect(index_page_view)


def edit_page(request,product_id):
        get_prod = ProductModel.objects.get(id=product_id)
        if request.method == 'POST':
             edit_product = ProductForm(request.POST,instance=get_prod)
             if edit_product.is_valid():
                  edit_product.save()
                  return redirect(index_page_view)
        context = {
             'form' : ProductForm(instance=get_prod)
        }
        return render(request,'productstore/edit.html',context)
