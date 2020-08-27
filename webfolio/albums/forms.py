"""albums FORMS Configuration"""
from django import forms
from .models import Image


class UploadImageForm(forms.ModelForm):
    """Upload image form"""

    class Meta:
        model = Image
        fields = ['name', 'imagefile']
