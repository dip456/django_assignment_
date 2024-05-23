from django.urls import path
from .views import *
    

urlpatterns = [
    path('admin/add-product/', admin_add_product, name='admin_add_product'),
    path('admin/add-product-sub-category/', admin_add_product_sub_category, name='admin_add_product_sub_category'),
    path('', admin_product_list, name='admin_product_list'),
    path('admin/edit-product/<int:pk>/', admin_edit_product, name='admin_edit_product'),
    path('admin/delete-product/<int:pk>/', admin_delete_product, name='admin_delete_product'),
    path('admin/edit-product-sub-category/<int:pk>/', admin_edit_product_sub_category, name='admin_edit_product_sub_category'),
    path('admin/delete-product-sub-category/<int:pk>/', admin_delete_product_sub_category, name='admin_delete_product_sub_category'),
    path('product-manager/search/', product_manager_search, name='product_manager_search'),
]
