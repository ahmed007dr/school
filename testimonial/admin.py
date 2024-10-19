from django.contrib import admin
from .models import Testimonial

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'rating')
    search_fields = ('name',)

admin.site.register(Testimonial, TestimonialAdmin)
