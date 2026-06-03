from django.db import models

# Create your models here.
class Song (models.Model):
    name = models.CharField(max_length=100)
    audio = models.FileField(upload_to='songs/')
    artist = models.CharField(max_length=100)
    image= models.ImageField(upload_to='song_images/')
    def __str__(self):
        return self.name
