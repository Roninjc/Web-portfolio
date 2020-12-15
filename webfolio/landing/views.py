from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from user.models import Image, Tag
from user.forms import UploadImageForm, CreateTagForm


def landpage(request, username):

    print(username)
    user = User.objects.get(username=username)
    print(user)
    galleries = Tag.objects.filter(user=user, is_a_gallery=True)

    context = {
        'galleries': galleries,
        }

    return render(request, 'landing/landpO.html', context)

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
