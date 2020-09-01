from django import forms
from django.core.exceptions import ValidationError
from api_programs.models import Program
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class Program_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Program
        fields = ('title', 'summary', 'body', 'image', 'type', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'restricted_to_positions': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Program name',
            'summary': 'Program description',
            'body': 'Program full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }

class Program_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Program
        fields = ('title', 'summary', 'body', 'image', 'type', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'restricted_to_positions': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Program name',
            'summary': 'Program description',
            'body': 'Program full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }

class Program_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Program
        fields = ('title', 'summary', 'body', 'image', 'type', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'restricted_to_positions': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Program name',
            'summary': 'Program description',
            'body': 'Program full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }
