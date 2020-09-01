from django.apps import AppConfig
from .models import Position
from django.db.models.signals import post_save


class WebAlbumConfig(AppConfig):
    name = 'web_albums'
