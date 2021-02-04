from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from user.models import Image, Tag, Profile
from user.forms import UploadImageForm, CreateTagForm

import json
from django.core.serializers.json import DjangoJSONEncoder


def landpage(request, username):

    user = User.objects.get(username=username)
    gallery_tags = Tag.objects.filter(user=user, is_a_gallery=True)
    profile = Profile.objects.get(user=user)
    background = profile.land_background.image_file
    art_name = profile.artistic_name

    context = {
        'art_name': art_name,
        'background': background,
        'gallery_tags': gallery_tags,
        'user': request.user,
        'username': username,
        }

    return render(request, 'landing/landpO.html', context)

def galleries(request, username):

    user = User.objects.get(username=username)
    gallery_tags = Tag.objects.filter(user=user, is_a_gallery=True)
    gallery_imgs = []
    for tag in gallery_tags:
        tag_img = Image.objects.filter(user=user, tags=tag, appear_in_album=True,)[:1]
        gallery_imgs.append(tag_img[0])
    galleries = [list(x) for x in zip(gallery_tags, gallery_imgs)]
    print(galleries)
    
    for gallery in galleries:
        img = gallery[1]
        print(img.image_file)

    context = {
        'gallery_tags': gallery_tags,
        'galleries': galleries,
        'username': username,
        }

    return render(request, 'landing/galleries.html', context)

def gallery(request, username, gallery):
    
    user = User.objects.get(username=username)
    gallery_tags = Tag.objects.filter(user=user, is_a_gallery=True)
    gallery_tag = Tag.objects.get(user=user, is_a_gallery=True, tag_name=gallery)
    
    uploaded_images = Image.objects.filter(user=user, tags=gallery_tag, appear_in_album=True)
    uploaded_images_values = uploaded_images.values()
    uploaded_images_values_json = json.dumps(list(uploaded_images_values), cls=DjangoJSONEncoder)
    
    context = {
        'gallery_tags': gallery_tags,
        'gallery_tag': gallery_tag,
        'uploaded_images': uploaded_images,
        'uploaded_images_values_json': uploaded_images_values_json,
        'username': username,
        }

    return render(request, 'landing/gallery.html', context)

def register(request):

    if request.method == 'POST':
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            username = registerForm.cleaned_data.get('username')
            raw_password = registerForm.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landing/landpO')
    else:
        registerForm = UserCreationForm()

    context = {
        'registerForm': registerForm,
        }

    return render(request, 'landing/register.html', context)
