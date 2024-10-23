from django.contrib import admin
from .models import BlogPost,AdditionalImage

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_posted')
    search_fields = ('title', 'author')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(AdditionalImage)