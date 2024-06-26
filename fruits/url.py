#urls.py (fruits_and_students/urls.py) 
from django.urls import path 
from .views import fruits_and_students 
urlpatterns = [ 
path('', fruits_and_students, name='fruits_and_students'), 
]
