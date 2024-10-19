# models.py
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    map_iframe = models.TextField()  # Use TextField for longer URLs

    def __str__(self):
        return self.name
