from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from bootstrap_modal_forms.forms import BSModalForm
from datetime import date
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from django.contrib.auth.forms import AuthenticationForm

class CreateUser_Login_Form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if ' ' in username:
            raise forms.ValidationError("User name cannot contain blanks.")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("User name already exists. Try a different user name.")
        return username

    def save(self, commit=True):
        user = super(CreateUser_Login_Form, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
