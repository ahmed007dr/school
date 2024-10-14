from django.shortcuts import render
from .models import AboutUs

def about_us(request):
    # Get the AboutUs instance (assuming there's only one)
    about_info = AboutUs.objects.first()
    
    context = {
        'about_info': about_info
    }
    
    return render(request, 'about.html', context)
