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

    tag1 = models.BooleanField()
    tag2 = models.BooleanField()
    tag3 = models.BooleanField()
    tag4 = models.BooleanField()
    tag5 = models.BooleanField()
    tag6 = models.BooleanField()
    tag7 = models.BooleanField()
    tag8 = models.BooleanField()
    tag9 = models.BooleanField()
    tag10 = models.BooleanField()

    def __str__(self,):
        return self.tag1
