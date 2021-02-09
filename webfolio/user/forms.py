"""user FORMS Configuration"""
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Image, Tag, Profile

import datetime


class UploadImageForm(forms.ModelForm):
    """Upload image form"""

    class Meta:
        model = Image
        fields = ['title', 'image_file', 'tags', 'appear_in_album']

    def __init__(self, user, *args, **kwargs):
        super(UploadImageForm, self).__init__(*args, **kwargs)
        self.fields['tags'].queryset = Tag.objects.filter(user=user)

    def save(self, request, commit=True):
        # Get the unsave Image instance
        self.instance.user = request.user
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           instance.tags.clear()
           instance.tags.add(*self.cleaned_data['tags'])
        self.save_m2m = save_m2m

        def set_dimension():
            Image.height = instance.image_file.height
            Image.width = instance.image_file.width_field
        self.set_dimension = set_dimension

        # Do we need to save all changes now?
        if commit:
            #if not instance.name:
                #self.created = datetime.datetime.today()
            #self.set_dimension()
            instance.save()
            self.save_m2m()

        return HttpResponseRedirect('imup')

class CreateTagForm(forms.ModelForm):
    """Create tag form"""

    class Meta:
        model = Tag
        fields = ['tag_name', 'is_a_gallery']
    
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_tag_name(self):
        tagname = self.cleaned_data['tag_name']
        if Tag.objects.filter(user=self.user, tag_name__iexact=tagname).exists():
            self.add_error('tag_name', ValidationError(_('This tag already exists.'), code='invalid'))
        return tagname

class ProfileForm(forms.ModelForm):
    """Profile options management form"""

    class Meta:
        model = Profile
        fields = [
            'artistic_name',
            'web_url',
            'logo',
            'land_background',
            'enable_about_me',
            'about_me',
            'enable_contact_me',
            'email',
            'enable_get_involved'
            ]

    def __init__(self, user, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['land_background'].queryset = Image.objects.filter(user=user)
