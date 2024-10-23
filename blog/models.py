from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date_posted = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title


class AdditionalImage(models.Model):
    blog_post = models.ForeignKey('BlogPost', related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/')
    description = models.TextField(blank=True, null=True)  # Optional description
