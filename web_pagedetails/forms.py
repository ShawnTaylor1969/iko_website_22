from django import forms
from django.core.exceptions import ValidationError
from api_pagedetails.models import PageDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class PageDetail_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = PageDetail
        fields = ('title',  'body')
        widgets = {
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
        }

class PageDetail_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = PageDetail
        fields = ('title',  'body')
        widgets = {
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
        }

class PageDetail_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = PageDetail
        fields = ('title',  'body')
        widgets = {
            'body': SummernoteWidget(attrs={'readonly':'readonly', 'summernote': {'width': '100%', 'height': '450px'}}),
        }
        
