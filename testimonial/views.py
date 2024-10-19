from django.shortcuts import render
from .models import Testimonial

def testimonial_view(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'testimonial/testimonial.html', {'testimonials': testimonials})

