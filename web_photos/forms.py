from django import forms
from django.core.exceptions import ValidationError
from api_photos.models import Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date
from django.forms import ClearableFileInput

class Photo_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Photo
        fields = ('title', 'summary', 'picture')
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 10}),
            'picture': ClearableFileInput(attrs={'multiple': True})
        }
        labels = {
            'picture': 'Click to upload picture(s)',
        }

class Photo_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Photo
        fields = ('title', 'summary', 'picture')
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 10}),
        }
        labels = {
            'picture': 'Click to upload an album cover image',
        }

class Photo_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Photo
        fields = ('title', 'summary', 'picture')
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 10}),
        }
        labels = {
            'picture': 'Click to upload an album cover image',
        }
