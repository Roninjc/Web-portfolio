"""albums VIEWS configuration"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib import messages

from .models import Image, Tag
from .forms import UploadImageForm, CreateTagForm

import time
import json


def upload_image(request):
    """Upload image form's view"""

    uploaded_images = Image.objects.all()
    for image in uploaded_images:
        tags_for_image = image.tags.all()
        print(uploaded_images)
        print(tags_for_image)

    if request.method == "POST":
        imageform = UploadImageForm(request.POST or None, request.FILES or None)
        if imageform.is_valid():
            imageform.save()
            messages.success(request, 'Image uploaded succesfully')
            return redirect('/albums/imup')
    else:
        imageform = UploadImageForm()

    context = {
        'imageform': imageform,
        'uploaded_images': uploaded_images,
        }

    return render(request, 'albums/images.html', context)

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
            err = tagform.errors.as_json()
            errDict = json.loads(err)
            for e in errDict.values():
                for m in e:
                    msg = m['message']
                    messages.error(request, msg)
            print(errDict)
            tagform = CreateTagForm()
    else:
        tagform = CreateTagForm()

    context = {
        'tagform': tagform,
        'created_tags': created_tags,
        }

    return render(request, 'albums/tags.html', context)

def delete_obj(request, mode, pk):
    """Delete speific object from database"""

    if mode == "imup":
        wh = "image"
        obj = get_object_or_404(Image, pk = pk)
    if mode == "tacr":
        wh = "tag"
        obj = get_object_or_404(Tag, pk = pk)

    if request.method == "POST":
        if wh == "imup":
            obj.image_file.delete()
        obj.delete()
        messages.success(request, wh.title() + ' removed succesfully')
        return redirect('/albums/' + mode)

    return render(request, 'albums/' + wh + 's.html', {'tag': tag})
