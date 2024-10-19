from django.urls import path
from .views import testimonial_view

urlpatterns = [
    path('pround', testimonial_view, name='testimonial-home'),
]
