from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)  
    feature1 = models.CharField(max_length=255)
    feature2 = models.CharField(max_length=255)
    feature3 = models.CharField(max_length=255)
    feature4 = models.CharField(max_length=255)
    feature5 = models.CharField(max_length=255)
    feature6 = models.CharField(max_length=255)
    more_details_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
