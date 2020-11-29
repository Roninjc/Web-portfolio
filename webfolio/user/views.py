"""user VIEWS configuration"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib import messages

from .models import Image, Tag
from .forms import UploadImageForm, CreateTagForm

import time
import json
from django.core.serializers.json import DjangoJSONEncoder

def user_panel(request):
    """User's config panel"""
    
    uploaded_images = Image.objects.all()
    n_images = len(uploaded_images)
    created_tags = Tag.objects.all()
    n_tags = len(created_tags)

    context = {
        'uploaded_images': uploaded_images,
        'n_images': n_images,
        'created_tags': created_tags,
        'n_tags': n_tags,
        }

    return render(request, 'user/panel.html', context)

def upload_image(request):
    """Upload image form's view"""

    uploaded_images = Image.objects.all()
    uploaded_images_values = uploaded_images.values()
    uploaded_images_values_json = json.dumps(list(uploaded_images_values), cls=DjangoJSONEncoder)
    
    if request.method == "POST":
        imageform = UploadImageForm(request.POST or None, request.FILES or None)
        if imageform.is_valid():
            imageform.save()
            messages.success(request, 'Image uploaded succesfully')
            return redirect('/user/imup')
    else:
        imageform = UploadImageForm()

    context = {
        'imageform': imageform,
        'uploaded_images': uploaded_images,
        'uploaded_images_values_json': uploaded_images_values_json,
        }

    return render(request, 'user/images.html', context)

def create_tags(request):
    
    """Create tags form's view"""
    
    created_tags = Tag.objects.all()

    if request.method == "POST":
        tagform = CreateTagForm(request.POST, request.FILES)
        if tagform.is_valid():
            tagform.save()
            messages.success(request, 'Tag added succesfully')
            return redirect('/user/tacr')
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

    return render(request, 'user/tags.html', context)

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
        return redirect('/user/' + mode)

    return render(request, 'user/' + wh + 's.html', {'tag': tag})
