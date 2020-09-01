from django import forms
from django.core.exceptions import ValidationError
from api_eventtypes.models import EventType
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class EventType_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = EventType
        fields = ('title',)

class EventType_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = EventType
        fields = ('title',)

class EventType_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = EventType
        fields = ('title',)
