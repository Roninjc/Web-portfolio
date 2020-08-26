from django.shortcuts import render
from .models import Image
from .forms import UploadImageForm

def upload_image_view(request):

    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile
    name = lastimage.name


    form = UploadImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()


    context = {'imagefile': imagefile, 'name': name, 'form': form}

    return render(request, 'albums/images.html', context)
