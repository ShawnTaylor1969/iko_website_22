from django import template
import requests
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from api_configurations.models import Configuration

register = template.Library()

@register.simple_tag
def getConfiguration():
    configuration = Configuration.objects.all().first()
    return configuration
