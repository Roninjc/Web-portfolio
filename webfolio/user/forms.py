"""user FORMS Configuration"""
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from .models import Image, Tag

import datetime


class UploadImageForm(forms.ModelForm):
    """Upload image form"""

    class Meta:
        model = Image
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
        fields = ['name', 'image_file', 'tags', 'appear_in_album']

    def __init__(self, *args, **kwargs):
        # Only in case we build the form from an instance
        # (otherwise, 'tags' list should be empty)
        if kwargs.get('instance'):
            # We get the 'initial' keyword argument or initialize it
            # as a dict if it didn't exist.                
            initial = kwargs.setdefault('initial', {})
            # The widget for a ModelMultipleChoiceField expects
            # a list of primary key for the selected data.
            initial['tags'] = [t.pk for t in kwargs['instance'].tag_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        # Get the unsave Image instance
        instance = forms.ModelForm.save(self, False)

        # Prepare a 'save_m2m' method for the form,
        old_save_m2m = self.save_m2m
        def save_m2m():
           old_save_m2m()
           instance.tags.clear()
           instance.tags.add(*self.cleaned_data['tags'])
        self.save_m2m = save_m2m

        def set_dimension():
            print(instance.image_file.height)
            Image.height = instance.image_file.height
            Image.width = instance.image_file.width
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

    def clean(self):
        cleaned_data = super(CreateTagForm, self).clean()
        tagname = cleaned_data.get('tag_name')
        if tagname and Tag.objects.filter(tag_name__iexact=tagname).exists():
            self.add_error('tag_name', ValidationError(_('This tag already exists.'), code='invalid'))
        return cleaned_data
