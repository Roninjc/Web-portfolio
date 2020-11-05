"""albums MODELS Configuration"""
from django.db import models

class Tag(models.Model):
    """Tags model"""

    tag_name = models.CharField(unique=True, blank=False, max_length=60)
    is_a_gallery = models.BooleanField(default=False)

    class Meta:
        ordering = ["tag_name"]

    def __str__(self,):
        return self.tag_name
        

class Image(models.Model):
    """Images model"""

    name = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to = 'albums/images/', unique=True)
    tags = models.ManyToManyField(Tag)
    appear_in_album = models.BooleanField(default=False)

    def __str__(self,):
        return self.name + ": " + str(self.image_file)
