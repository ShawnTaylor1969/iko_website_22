from django import forms
from api_members.models import Member
from api_spaces.models import Space
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import slugify
import itertools

class Member_Sister_Filter_Form(forms.Form):
    search                  = forms.CharField(widget=forms.HiddenInput(), required=False)
    name                    = forms.CharField(max_length=200, strip=True, required=False)
    pledge_class            = forms.CharField(max_length=4, strip=True, required=False)
    graduation_year         = forms.CharField(max_length=4, strip=True, required=False)

    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

class Member_Form(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = Member
        fields = ('type', 'about_me', 'pledge_class', 'graduation_year', 'birth_date', 'picture')
        widgets = {'about_me': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}} )}

# *_EditForm are used by the Site Administrator
class User_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')

class Member_EditForm(forms.ModelForm):
    PLEDGECLASS_CHOICES = []
    firstYear = date.today().year - 80
    currentYear = date.today().year + 1
    for year in range(firstYear,currentYear +1 ):
        strYear = str(year)
        PLEDGECLASS_CHOICES.append((strYear, strYear))

    GRADUATIONYEAR_CHOICES = []
    for year in range(firstYear,currentYear +1 ):
        strYear = str(year)
        GRADUATIONYEAR_CHOICES.append((strYear, strYear))

    pledgeClass = forms.ChoiceField(label="Pledge class", choices=PLEDGECLASS_CHOICES)
    graduationYear = forms.ChoiceField(label="Graduation year", choices=GRADUATIONYEAR_CHOICES)

    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = Member
        fields = ('type', 'pledgeClass', 'graduationYear', 'birth_date', 'picture', 'about_me', 'status')
        widgets = {
            'about_me': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'birth_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'birth_date': 'Birth date',
            'profile_picture': 'Click to upload an image',
        }

class Edit_UserForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class Edit_MemberForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = Member
        fields = ('birth_date', 'picture', 'about_me')
        widgets = {
            'about_me': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '450px'}}),
            'birth_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'birth_date': 'Birth date',
            'profile_picture': 'Click to upload an image',
        }

class Member_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = Member
        fields = ('about_me',  'birth_date', 'picture')
        widgets = {
            'about_me': SummernoteWidget(attrs={'readonly':'readonly', 'summernote': {'width': '100%', 'height': '450px'}}),
            'birth_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'birth_date': 'Birth date',
            'profile_picture': 'Click to upload an image',
        }

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

    def clean(self):
        cleaned_data = super().clean()

        # Since each user has a space, make sure that the slug associated with the resulting space
        # does not already exist.
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if Space.objects.filter(title=first_name + " " + last_name):
            raise forms.ValidationError("Combination of first and last name already exists.")

        value = "User space " + first_name + " "  + last_name
        slug_candidate = slug_original = slugify(value, allow_unicode=True)
        for i in itertools.count(1):
            if not Space.objects.filter(slug=slug_candidate).exists():
                break
            slug_candidate = '{}-{}'.format(slug_original, i)

        if Space.objects.filter(slug=slug_candidate).exists():
            raise forms.ValidationError("Combination of first and last name already exists.")

    def save(self, commit=True):
        user = super(CreateUser_Login_Form, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CreateUser_Member_Form(forms.ModelForm):
    PLEDGECLASS_CHOICES = []
    firstYear = date.today().year - 80
    currentYear = date.today().year + 1
    for year in range(firstYear,currentYear +1 ):
        strYear = str(year)
        PLEDGECLASS_CHOICES.append((strYear, strYear))

    GRADUATIONYEAR_CHOICES = []
    for year in range(firstYear,currentYear +1 ):
        strYear = str(year)
        GRADUATIONYEAR_CHOICES.append((strYear, strYear))

    pledgeClass = forms.ChoiceField(label="Pledge class", choices=PLEDGECLASS_CHOICES)
    graduationYear = forms.ChoiceField(label="Graduation year", choices=GRADUATIONYEAR_CHOICES)

    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True
    class Meta:
        startYear = date.today().year-85
        endYear = date.today().year-15
        model = Member
        fields = ('type', 'pledgeClass', 'graduationYear', 'birth_date')
        widgets = {
            'birth_date': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'type': 'Reason for the login account'
        }

    def clean(self):
        cleaned_data = super().clean()
        pledge_class = int(cleaned_data.get('pledgeClass'))
        graduation_year = int(cleaned_data.get('graduationYear'))
        type = cleaned_data.get('type')
        currentYear = date.today().year

        if (pledge_class > graduation_year):
            raise forms.ValidationError("Pledge class cannot be after your graduation year. Please correct the pledge class or graduation year and resubmit.")
        if not pledge_class == currentYear and type == "NEWBLOOD" :
            raise forms.ValidationError("Signing up to a past pledge class suggests that you are not a new blood.  Please correct the pledge class or status and resubmit.")
        if graduation_year < currentYear - 1 and not type == "ALUMNI" :
            raise forms.ValidationError("Graduation year suggests that your are an alumni.  Please correct the graduation year or status and resubmit.")

        return cleaned_data

class CustomAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active or not user.member_profile:
            raise forms.ValidationError('There was a problem with your login. Check with website webmaster.', code='invalid_login')
        elif not user.member_profile.status == 'ACTIVATED':
            raise forms.ValidationError('You cannot login until your identity has been validated.', code='waiting_on_validation')
