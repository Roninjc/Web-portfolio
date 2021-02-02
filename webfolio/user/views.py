"""user VIEWS configuration"""
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Image, Tag, Profile
from .forms import UploadImageForm, CreateTagForm, ProfileForm

import time
import json
from django.core.serializers.json import DjangoJSONEncoder

@login_required
def user_panel(request):
    """User's config panel"""
    
    uploaded_images = Image.objects.filter(user=request.user)
    n_images = len(uploaded_images)
    created_tags = Tag.objects.filter(user=request.user)
    n_tags = len(created_tags)

    try:
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            profileform = ProfileForm(request.user, request.POST, instance=profile)
            if profileform.is_valid():
                instance = profileform.instance
                instance.user = request.user
                instance.save()

                return redirect('/user')
        else:
            profileform = ProfileForm(request.user, instance=profile)
    except Profile.DoesNotExist:
        if request.method == "POST":
            profileform = ProfileForm(request.user, request.POST)
            if profileform.is_valid():
                instance = profileform.instance
                instance.user = request.user
                instance.save()

                return redirect('/user')
        else:
            profileform = ProfileForm(request.user)

    context = {
        'uploaded_images': uploaded_images,
        'n_images': n_images,
        'created_tags': created_tags,
        'n_tags': n_tags,
        'user': request.user,
        'profileform': profileform
        }

    return render(request, 'user/panel.html', context)

@login_required
def upload_image(request):
    """Upload image form's view"""

    uploaded_images = Image.objects.filter(user=request.user)
    uploaded_images_values = uploaded_images.values()
    uploaded_images_values_json = json.dumps(list(uploaded_images_values), cls=DjangoJSONEncoder)
    
    if request.method == "POST":
        imageform = UploadImageForm(request.user, request.POST or None, request.FILES or None)
        if imageform.is_valid():
            imageform.save(request)
            messages.success(request, 'Image uploaded succesfully')
            return redirect('/user/imup')
    else:
        imageform = UploadImageForm(request.user)

    context = {
        'imageform': imageform,
        'uploaded_images': uploaded_images,
        'uploaded_images_values_json': uploaded_images_values_json,
        }

    return render(request, 'user/images.html', context)

@login_required
def create_tags(request):
    
    """Create tags form's view"""
    
    created_tags = Tag.objects.filter(user=request.user)

    if request.method == "POST":
        tagform = CreateTagForm(request.POST, request.FILES)
        if tagform.is_valid():
            instance = tagform.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'Tag added succesfully')
            return redirect('/user/tacr')
        else:
            err = tagform.errors.as_json()
            errDict = json.loads(err)
            for e in errDict.values():
                for m in e:
                    msg = m['message']
                    messages.error(request, msg)
            tagform = CreateTagForm()
    else:
        tagform = CreateTagForm()

    context = {
        'tagform': tagform,
        'created_tags': created_tags,
        }

    return render(request, 'user/tags.html', context)

@login_required
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

def logout(request):

    return render(request, 'user/logout.html')
