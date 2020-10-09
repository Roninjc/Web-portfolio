"""albums VIEWS configuration"""
from django.shortcuts import render

from .models import Image, Tag
from .forms import UploadImageForm, CreateTagForm

def upload_image(request):
    """Upload image form's view"""

    """
    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile
    name = lastimage.name
    ide = lastimage.id
    """


    imageform = UploadImageForm(request.POST or None, request.FILES or None)
    if imageform.is_valid():
        imageform.save()

    context = {
        'imageform': imageform,
        }

    return render(request, 'albums/images.html', context)

def create_tags(request):
    """Create tags form's view"""



    tagform = CreateTagForm(request.POST or None, request.FILES or None)
    if tagform.is_valid():
        tagform.save()



    context = {'tagform': tagform}

    return render(request, 'albums/tags.html', context)