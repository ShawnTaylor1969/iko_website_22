from django import template
import requests
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from api_configurations.models import Configuration

register = template.Library()

@register.simple_tag
def getConfiguration(base_url='http://127.0.0.1:8000'):
    # Check to see if the user has access to the space
    response = requests.get(base_url + reverse('api_configurations:read'))
    configuration = response.json()
    return configuration
