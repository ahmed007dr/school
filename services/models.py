from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)  
    image_serv =models.ImageField(upload_to='images/', blank=True, null=True)  

    def __str__(self):
        return self.title
