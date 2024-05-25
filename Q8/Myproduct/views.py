from django.shortcuts import render,redirect,get_object_or_404

from .models import Product
from .models import ProductSubCat
from .forms import ProductForm
from .forms import ProductSubCatForm
# Create your views here.
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
        context = {
            'form':form
        }
    return render(request, 'Myproduct/add_product.html', context)

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Myproduct/product_list.html',context)

def add_product_subcat(request):
    if request.method == "POST":
        form = ProductSubCatForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_subcat_list')
    else:
        form = ProductSubCatForm()
        context = {
            'form': form
        }
    return render(request, 'Myproduct/add_product_subcat.html', context)

def product_subcat_list(request):
    subcats = ProductSubCat.objects.all()
    query = request.GET.get('q')


    context = {
        'subcats': subcats,
    }
    if query:
        products = product.filter(product__product_name__icontains=query)
    return render(request, 'Myproduct/product_subcat_list.html',context)

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        context = {
            'form': form
        }
    return render(request, 'Myproduct/edit_product.html',context)

def edit_product_sub_category(request, pk):
    product_sub_cat = get_object_or_404(ProductSubCat, pk=pk)
    if request.method == 'POST':
        form = ProductSubCatForm(request.POST, instance=product_sub_cat)
        if form.is_valid():
            form.save()
            return redirect('product_subcat_list')
    else:
        form = ProductSubCatForm(instance=product_sub_cat)
        context = {
            'form': form
        }
    return render(request, 'Myproduct/edit_subcate.html',context)

def delete_category(request, pk):
    product_sub_cat = get_object_or_404(ProductSubCat, pk=pk)
    product_sub_cat.delete()
    return redirect('product_subcat_list')







 