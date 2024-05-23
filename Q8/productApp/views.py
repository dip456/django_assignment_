from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductSubCategory
from .forms import ProductForm, ProductSubCategoryForm

def admin_add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm()
    return render(request, 'productApp/admin_add_product.html', {'form': form})

def admin_add_product_sub_category(request):
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductSubCategoryForm()
    return render(request, 'productApp/admin_add_product_sub_category.html', {'form': form})

def admin_product_list(request):
    products = Product.objects.all()
    return render(request, 'productApp/admin_product_list.html', {'products': products})

def admin_edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'productApp/admin_edit_product.html', {'form': form})

def admin_delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('admin_product_list')

def admin_edit_product_sub_category(request, pk):
    sub_category = get_object_or_404(ProductSubCategory, pk=pk)
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES, instance=sub_category)
        if form.is_valid():
            form.save()
            return redirect('admin_product_list')
    else:
        form = ProductSubCategoryForm(instance=sub_category)
    return render(request, 'productApp/admin_edit_product_sub_category.html', {'form': form})

def admin_delete_product_sub_category(request, pk):
    sub_category = get_object_or_404(ProductSubCategory, pk=pk)
    sub_category.delete()
    return redirect('admin_product_list')

def product_manager_search(request):
    query = request.GET.get('query', '')
    products = ProductSubCategory.objects.filter(product__name__icontains=query)
    return render(request, 'productApp/product_manager_search.html', {'products': products, 'query': query})
