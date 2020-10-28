"""albums VIEWS configuration"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib import messages

from .models import Image, Tag
from .forms import UploadImageForm, CreateTagForm

import time


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
        return redirect('/albums/imup')

    context = {
        'imageform': imageform,
        }

    return render(request, 'albums/images.html', context)

@never_cache
def create_tags(request):
    
    """Create tags form's view"""
    
    created_tags = Tag.objects.all()

    if request.method == "POST":
        tagform = CreateTagForm(request.POST, request.FILES)
        if tagform.is_valid():
            tagform.save()
            messages.success(request, 'Tag added succesfully')
            return redirect('/albums/tacr')
    else:
        tagform = CreateTagForm()

    context = {
        'tagform': tagform,
        'created_tags': created_tags,
        }

    return render(request, 'albums/tags.html', context)

def delete_obj(request, pk):
    """Delete speific object from database"""

    obj = get_object_or_404(Tag, pk = pk)

    if request.method == "POST":
        obj.delete()
        return redirect('/albums/tacr')

    return render(request, 'albums/tags.html', {'tag': tag})
