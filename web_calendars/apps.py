from django.apps import AppConfig
from .models import Position
from django.db.models.signals import post_save


class WebCalendarConfig(AppConfig):
    name = 'web_calendars'
