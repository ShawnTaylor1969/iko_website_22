from django import template
import requests
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.models import User
from api_spacelinks.models import SpaceLink

register = template.Library()

@register.simple_tag
def get_spacelinks(space_slug=None, root_slug=None):
    return SpaceLink.objects.filter(space__slug=space_slug, parent__slug=root_slug).order_by('sequence')

@register.simple_tag
def get_user_links(spacelink_slug='top-left', user=None):
    # treeItems = TreeItem.objects.filter(root__slug=tree_slug).filter(parent=None).order_by('sequence')
    # authorized_pks = []
    # for treeItem in treeItems:
    #     if is_authorized(treeItem, user):
    #         authorized_pks.append(treeItem.pk)
    # treeItems = TreeItem.objects.filter(pk__in=authorized_pks).order_by('sequence')
    return SpaceLink.objects.filter(parent__slug=spacelink_slug).order_by('sequence')
