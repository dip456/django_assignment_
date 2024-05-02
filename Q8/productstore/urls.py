from django.contrib import admin
from django.urls import path

from .views import index_page_view
from .views import delete_page
from .views import edit_page


urlpatterns = [
    path('',index_page_view,name='index_page_view'),
    path('delete/<int:product_id>',delete_page,name='delete_page'),
    path('edit/<int:product_id>/',edit_page, name='edit_page')
]