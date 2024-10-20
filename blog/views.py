from django.shortcuts import render ,get_object_or_404
from .models import BlogPost

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-date_posted')
    return render(request, 'blog/blog.html', {'posts': posts})


def blog_post_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})
