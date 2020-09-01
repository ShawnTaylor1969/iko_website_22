from django import template
from django.contrib.auth.models import User
from api_spaces.models import Space
from api_spacelinks.models import SpaceLink

register = template.Library()


@register.inclusion_tag('web_spaces/left_sidebar_spacelinks.html')
def left_sidebar_spacelinks(user=None, space_slug=None):
    space = Space.objects.get(slug=space_slug)
    parent_slug = space_slug + "-" + space_slug + "-links"
    spacelinks= SpaceLink.objects.filter(space__slug=space_slug, parent__slug=parent_slug).order_by('sequence')
    return {'space': space, 'spacelinks': spacelinks, 'user': user}
