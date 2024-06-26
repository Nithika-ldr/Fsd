#urls.py (website_pages /urls.py) 
from django.urls import path 
from website_pages import views 
urlpatterns = [ 
path('home/', views.home, name='home'), 
path('about_us/', views.about_us, name='about_us'), 
path('contact_us/', views.contact_us, name='contact_us'), 
]
