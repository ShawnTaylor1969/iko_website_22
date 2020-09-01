from django import forms
from django.core.exceptions import ValidationError
from api_walls.models import Wall
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class Wall_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Wall
        fields = ('picture',  'title', 'message')
        widgets = {
            'message': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
        }
        labels = {
            'picture': 'Click to upload a picture',
        }

class Wall_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Wall
        fields = ('picture',  'title', 'message')
        widgets = {
            'message': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
        }
        labels = {
            'picture': 'Click to upload a picture',
        }

class Wall_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Wall
        fields = ('picture',  'title', 'message')
        widgets = {
            'message': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
        }
        labels = {
            'picture': 'Click to upload a picture',
        }
