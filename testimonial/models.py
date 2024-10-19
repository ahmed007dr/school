from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    message = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.name
