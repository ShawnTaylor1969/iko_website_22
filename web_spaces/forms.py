from django import forms
from django.core.exceptions import ValidationError
from api_spaces.models import Space
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class Space_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Space
        fields = ('title', 'summary', 'body', 'image', 'content_types', 'type','layout', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'admin_method', 'admin_position', 'admin_user', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'content_types': forms.CheckboxSelectMultiple(),
            'restricted_to_positions': forms.CheckboxSelectMultiple(),
            'restricted_to_groups': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Space name',
            'summary': 'Space description',
            'body': 'Space full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if cleaned_data.get("parent_position") == self.instance:
    #         raise ValidationError("Parent position cannot be itself.")
    #
    #     if cleaned_data.get("is_top_five") == False and cleaned_data.get("parent_position") == None:
    #         raise ValidationError("Parent position is required when the position is not Top Five.")
    #     return cleaned_data

class Space_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Space
        fields = ('title', 'summary', 'body', 'image', 'content_types', 'type','layout', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'admin_method', 'admin_position', 'admin_user', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'content_types': forms.CheckboxSelectMultiple(),
            'restricted_to_positions': forms.CheckboxSelectMultiple(),
            'restricted_to_groups': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Space name',
            'summary': 'Space description',
            'body': 'Space full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     if cleaned_data.get("parent_position") == self.instance:
    #         raise ValidationError("Parent position cannot be itself.")
    #
    #     if cleaned_data.get("is_top_five") == False and cleaned_data.get("parent_position") == None:
    #         raise ValidationError("Parent position is required when the position is not Top Five.")
    #     return cleaned_data

class Space_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Space
        fields = ('title', 'summary', 'body', 'image', 'content_types', 'type','layout', 'url', \
                    'show_space_menu','show_application_menu', 'public_access', 'private_access', \
                    'restricted_access', 'restricted_to_positions', 'restricted_to_groups', 'admin_method', 'admin_position', 'admin_user', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'autofocus': 'autofocus'}, ),
            'summary': forms.Textarea(attrs={'rows':4}),
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'content_types': forms.CheckboxSelectMultiple(),
            'restricted_to_positions': forms.CheckboxSelectMultiple(),
            'restricted_to_groups': forms.CheckboxSelectMultiple()
        }
        labels = {
            'title': 'Space name',
            'summary': 'Space description',
            'body': 'Space full description',
            'public_access': 'Public access (Available to non-members i.e. the public via the Internet)',
            'private_access': 'Private access (Available to members)',
            'restricted_access': 'Restricted to specific members',
            'restricted_to_positions': 'Restricted to (by position)',
            'restricted_to_groups': 'Restricted to (by group)',
            'image': 'Click to upload an image'
        }
