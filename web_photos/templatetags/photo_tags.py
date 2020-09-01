from django import template

register = template.Library()

@register.simple_tag
def get_image_size(width, height):
    width_height_ratio = width / height
    retval = "normal"
    if width_height_ratio <= .7:
        retval = "tall"
    if width_height_ratio >= 1.5:
        retval = "wide"
    if width > 1000:
        retval = "big"
    return retval
