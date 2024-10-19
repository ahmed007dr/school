from django.shortcuts import render
from .models import BlogPost

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'posts': posts})
