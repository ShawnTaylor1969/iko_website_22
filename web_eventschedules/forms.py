from django import forms
from django.core.exceptions import ValidationError
from api_eventschedules.models import EventSchedule
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.forms.widgets import CheckboxSelectMultiple
from dal import autocomplete, forward
from datetime import date

class EventSchedule_CreateForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year
        endYear = date.today().year + 5
        model = EventSchedule
        fields = ('event_type',  'title', 'organizer', 'body', 'picture', 'is_active', \
                    'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                    'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'weekly_frequency', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                    'repeat_on_Mon', 'repeat_on_Tue', 'repeat_on_Wed', 'repeat_on_Thu', 'repeat_on_Fri', 'repeat_on_Sat', 'repeat_on_Sun', \
                    'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', 'end_series', 'series_occurrences', \
                    'location', 'show_as_busy')
        widgets = {
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'public_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'independent_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'active_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'alumni_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'start_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
            'end_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'start_dateTime': 'Start date',
            'end_dateTime': 'End date',
            'public_body_same_as': 'Present the same body to the public?',
            'independent_body_same_as': 'Present the same body to independents?',
            'active_body_same_as': 'Present the same body to the actives?',
            'alumni_body_same_as': 'Present the same body to the alumni?',
            'is_active': 'Is an active schedule?',
            'picture': 'Click to upload an image',
        }

class EventSchedule_EditForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year
        endYear = date.today().year + 5
        model = EventSchedule
        fields = ('event_type',  'title', 'organizer', 'body', 'picture', 'is_active', \
                    'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                    'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'weekly_frequency', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                    'repeat_on_Mon', 'repeat_on_Tue', 'repeat_on_Wed', 'repeat_on_Thu', 'repeat_on_Fri', 'repeat_on_Sat', 'repeat_on_Sun', \
                    'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', 'end_series', 'series_occurrences', \
                    'location', 'show_as_busy')
        widgets = {
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'public_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'independent_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'active_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'alumni_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'start_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
            'end_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'start_dateTime': 'Start date',
            'end_dateTime': 'End date',
            'public_body_same_as': 'Present the same body to the public?',
            'independent_body_same_as': 'Present the same body to independents?',
            'active_body_same_as': 'Present the same body to the actives?',
            'alumni_body_same_as': 'Present the same body to the alumni?',
            'is_active': 'Is an active schedule?',
            'picture': 'Click to upload an image',
        }

class EventSchedule_ReadForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.disable_csrf = True

    class Meta:
        startYear = date.today().year
        endYear = date.today().year + 5
        model = EventSchedule
        fields = ('event_type',  'title', 'organizer', 'body', 'picture', 'is_active', \
                    'public_body_same_as', 'public_body', 'independent_body_same_as', 'independent_body', 'active_body_same_as', 'active_body', 'alumni_body_same_as', 'alumni_body', \
                    'start_dateTime', 'end_dateTime', 'all_day_event', 'frequency', 'repeat_every_n_days', 'weekly_frequency', 'repeat_every_n_weeks', 'repeat_week_of_month', \
                    'repeat_on_Mon', 'repeat_on_Tue', 'repeat_on_Wed', 'repeat_on_Thu', 'repeat_on_Fri', 'repeat_on_Sat', 'repeat_on_Sun', \
                    'repeat_last_day_of_month', 'repeat_day_of_the_month', 'repeat_every_n_years', 'end_series', 'series_occurrences', \
                    'location', 'show_as_busy')
        widgets = {
            'body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'public_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'independent_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'active_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'alumni_body': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '350px'}}),
            'start_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
            'end_dateTime': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day"), years=range(startYear, endYear), attrs=({'style': 'width: 33%; display: inline-block;'})),
        }
        labels = {
            'start_dateTime': 'Start date',
            'end_dateTime': 'End date',
            'public_body_same_as': 'Present the same body to the public?',
            'independent_body_same_as': 'Present the same body to independents?',
            'active_body_same_as': 'Present the same body to the actives?',
            'alumni_body_same_as': 'Present the same body to the alumni?',
            'is_active': 'Is an active schedule?',
            'picture': 'Click to upload an image',
        }
