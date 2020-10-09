"""albums FORMS Configuration"""
from django import forms
from .models import Image, Tag


class UploadImageForm(forms.ModelForm):
    """Upload image form"""

    class Meta:
        model = Image
        tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
        fields = ['name', 'imagefile', 'tags']

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
           # This is where we actually link the pizza with tags
           instance.tag_set.clear()
           instance.tag_set.add(*self.cleaned_data['tags'])
        self.save_m2m = save_m2m

        # Do we need to save all changes now?
        if commit:
            instance.save()
            self.save_m2m()

        return instance

class CreateTagForm(forms.ModelForm):
    """Create tag form"""

    class Meta:
        model = Tag
        fields = ['tagname', 'appearinalbum']
