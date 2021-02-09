"""user MODELS Configuration"""
from django.db import models
from django.contrib.auth.models import User
import datetime

class Tag(models.Model):
    """Tags model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag_name = models.CharField(blank=False, max_length=60)
    is_a_gallery = models.BooleanField(default=False)

    class Meta:
        ordering = ["tag_name"]

    def __str__(self):
        return self.tag_name
        
class Image(models.Model):
    """Images model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
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

    def __str__(self):
        return self.title

    def save(self):
        if not self.id:
            self.created = datetime.datetime.today()
        self.updated = datetime.datetime.today()
        super(Image, self).save()

class Profile(models.Model):
    """Profiles model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    artistic_name = models.CharField(max_length=50)
    web_url = models.CharField(max_length=30, blank=True)
    logo = models.ImageField(upload_to = 'landing/logos/', blank=True)
    land_background = models.OneToOneField(Image, on_delete=models.CASCADE, null=True, blank=True, verbose_name="homepage bakground")
    enable_about_me = models.BooleanField(default=True)
    about_me = models.TextField(blank=True)
    enable_contact_me = models.BooleanField(default=True)
    email = models.EmailField(blank=True)
    enable_get_involved = models.BooleanField(default=True)

    def __str__(self):
        return self.artistic_name
