from django import template

register = template.Library()

@register.inclusion_tag('web_eventschedules/upcoming_events.html')
def show_upcoming_events(events, cols=1, width=100, height=100, media_body_min_height=100, border='False'):
    return {'events': events, 'cols': cols, 'width': width, 'height': height, 'media_body_min_height': media_body_min_height, 'border': border}

@register.simple_tag
def get_short_month(source_date):
    return source_date.strftime('%B')[0:3]

@register.simple_tag
def get_short_day(source_date):
    return source_date.day
