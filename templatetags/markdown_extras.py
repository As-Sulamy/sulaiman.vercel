from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown(text):
    if not text:
        return ''
    return mark_safe(markdown.markdown(text, extensions=['extra', 'codehilite', 'tables']))

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter(name='trim')
def trim(value):
    return value.strip()
