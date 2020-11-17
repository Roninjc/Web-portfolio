from django.shortcuts import render

from albums.models import Image, Tag
from albums.forms import UploadImageForm, CreateTagForm


def landpage(request):

    created_tags = Tag.objects.all()
    galleries = Tag.objects.filter(is_a_gallery=True)

    context = {
        'created_tags': created_tags,
        'galleries': galleries,
        }

    return render(request, 'landing/landpO.html', context)
