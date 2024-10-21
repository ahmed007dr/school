from django.shortcuts import render
from .models import Settingz

def gallery_view(request):
    images = Settingz.objects.all()
    return render(request, 'templates/base.html', {'images': images})
