"""What is Django URLs?make program to create django urls"""
"""
Django URLs : used to specify the web addresses or paths within a web application. These URLs are mapped to corresponding view functions, 
allowing Django to determine how to handle incoming requests. 


1. create app :
   python manage.py startapp demo_app

2. cretae view :
   from django.http import HttpResponse

   def home_view(request):
       return HttpResponse("hii")

3. create urls in urls.py file 
   from django.urls import path
   from . import views *

   urlpatterns = [
       path('', home_view, name='home_view'),
    ]

4. project in urls.py 

   from django.contrib import admin
   from django.urls import path,include

   urlpatterns = [
      path('admin/', admin.site.urls),
      path('', include('demo_app.urls')),
   ]

5. run project :
   python manage.py runserver

       
    

"""