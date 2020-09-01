from django import forms
from django.core.exceptions import ValidationError
from api_positions.models import Position
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class Position_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    helper.layout = Layout(
        Field('title'),
        Field('is_top_five', onchange='form_change_js(this,"/positions/create")'),
        Field('parent_position')
    )
    class Meta:
        model = Position
        fields = ('title', 'is_top_five', 'parent_position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_position'].queryset = Position.objects.filter(is_top_five=True)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("parent_position") == self.instance:
            raise ValidationError("Parent position cannot be itself.")

        if cleaned_data.get("is_top_five") == False and cleaned_data.get("parent_position") == None:
            raise ValidationError("Parent position is required when the position is not Top Five.")
        return cleaned_data

class Position_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    helper.layout = Layout(
        Field('title'),
        Field('is_top_five', onchange='form_change_js(this,"/positions/edit")'),
        Field('parent_position')
    )
    class Meta:
        model = Position
        fields = ('title', 'is_top_five', 'parent_position')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_position'].queryset = Position.objects.filter(is_top_five=True)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get("parent_position") == self.instance:
            raise ValidationError("Parent position cannot be itself.")

        if cleaned_data.get("is_top_five") == False and cleaned_data.get("parent_position") == None:
            raise ValidationError("Parent position is required when the position is not Top Five.")
        return cleaned_data

class Position_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    helper.layout = Layout(
        Field('title'),
        Field('is_top_five', onchange='form_change_js(this,"/positions/create")'),
        Field('parent_position')
    )
    class Meta:
        model = Position
        fields = ('title', 'is_top_five', 'parent_position')
