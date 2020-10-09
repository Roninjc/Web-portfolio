"""albums MODELS Configuration"""
from django.db import models

class Tag(models.Model):
    """Tags model"""

    tagname = models.CharField(max_length=60)
    appearinalbum = models.BooleanField(default=False)

    def __str__(self,):
        return self.tagname

class Image(models.Model):
    """Images model"""

    name = models.CharField(max_length=200)
    imagefile = models.ImageField(upload_to = 'albums/images/')
    tags = models.ManyToManyField(Tag)

    def __str__(self,):
        return self.name + ": " + str(self.imagefile)
