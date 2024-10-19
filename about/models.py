from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    image_long=models.ImageField(upload_to='images/', blank=True, null=True)  
    more_details_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
