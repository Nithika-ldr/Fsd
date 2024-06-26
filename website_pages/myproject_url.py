#urls.py (myproject/urls.py)
from django.contrib import admin 
from django.urls import path, include 
urlpatterns = [ 
path("", include("myapp.urls")), 
path("admin/", admin.site.urls), 
path('fruits_and_students/', include('fruits_and_students.urls')), 
path('', include('website_pages.urls')), 
]
