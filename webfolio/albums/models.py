from django.db import models

# Create your models here.


class Image(models.Model):
    name = models.CharField(max_length=200)
    imagefile = models.ImageField(upload_to = 'albums/images/')

    def __str__(self,):
        return self.name + ": " + str(self.imagefile)
