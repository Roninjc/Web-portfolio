"""albums MODELS Configuration"""
from django.db import models

# Create your models here.


class Image(models.Model):
    """Images model"""

    name = models.CharField(max_length=200)
    imagefile = models.ImageField(upload_to = 'albums/images/')

    def __str__(self,):
        return self.name + ": " + str(self.imagefile)

class Tag(models.Model):
    """Tags model"""

    tagname = models.CharField(max_length=60)
    appearinalbum = models.BooleanField(default=True)

    def __str__(self,):
        return self.tagname
