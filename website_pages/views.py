from django.shortcuts import render 
def home(request): 
return render(request, 'website_pages/home.html') 
def about_us(request): 
return render(request, 'website_pages/about_us.html') 
def contact_us(request): 
return render(request, 'website_pages/contact_us.html')
