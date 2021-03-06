from django import template

register = template.Library()

from ..models import Product, THUMBNAIL_CHOICES

@register.filter
def get_thumbnail(obj, arg):
    arg = arg.lower()
    if not isinstance(obj, Product):
        raise TypeError("This is not a valid product model.")
    choices = dict(THUMBNAIL_CHOICES)
    if not choices.get(arg):
        raise TypeError("This is not a valid type for the model.")
    try:
        return obj.thumbnail_set.filter(type=arg).first().media.url
    except:
        return None