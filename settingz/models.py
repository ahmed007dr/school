from django.db import models

class Settingz(models.Model):
    address = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    facebook = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    title_logo = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20)
    site_name = models.CharField(max_length=100)
    design_by = models.CharField(max_length=100, blank=True, null=True)
    long_banner = models.ImageField(upload_to='images/', blank=True, null=True)  
    def __str__(self):
        return self.site_name
