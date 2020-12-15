"""user MODELS Configuration"""
from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    """Tags model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(unique=True, blank=False, max_length=60)
    is_a_gallery = models.BooleanField(default=False)

    class Meta:
        ordering = ["tag_name"]

    def __str__(self,):
        return self.tag_name
        
class Image(models.Model):
    """Images model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image_file = models.ImageField(
        upload_to = 'user/images/',
        unique=True,
        height_field='height',
        width_field='width')
    height = models.IntegerField(editable=False)
    width = models.IntegerField(editable=False)
    tags = models.ManyToManyField(Tag)
    appear_in_album = models.BooleanField(default=False)
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def __str__(self,):
        return self.name + ": " + str(self.image_file) + str(self.tags)

    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Image, self).save()


