"""albums VIEWS configuration"""
from django.shortcuts import render

from .models import Image
from .forms import UploadImageForm

def upload_image_view(request):
    """Upload image form's view"""

    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile
    name = lastimage.name
    ide = lastimage.id


    form = UploadImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()



    context = {'imagefile': imagefile, 'name': name, 'ide': ide, 'form': form}

    return render(request, 'albums/images.html', context)
