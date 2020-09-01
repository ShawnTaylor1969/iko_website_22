from django import template
from api_members.models import Member
from api_spaces.models import Space

register = template.Library()

@register.filter
def replace_user_pk(value, user_pk):
    space = Space.objects.get(user_space=True, admin_user__pk=user_pk)
    retval = value
    retval = retval.replace("--space_pk--", str(space.pk))
    retval = retval.replace("--user_pk--", str(user_pk))
    return retval

@register.simple_tag
def get_member(user):
    # Check to see if the user has access to the space
    member = Member.objects.get(user=user)
    return member

@register.inclusion_tag('web_members/dummy.html')
def format_birthdays_as_webpage_area(record=None):
    template = 'web_members/events_birthdays.html'
    return {'template': template, 'record': record}
