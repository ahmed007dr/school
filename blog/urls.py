from django.urls import path
from .views import blog_view ,single_blog

urlpatterns = [
    path('blog/', blog_view, name='blog-home'),
    path('blog/<int:post_id>/', single_blog, name='single_blog'),

]
