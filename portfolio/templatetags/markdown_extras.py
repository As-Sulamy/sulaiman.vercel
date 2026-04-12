from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown(text):
    import markdown
    return mark_safe(markdown.markdown(text))

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)

@register.filter(name='trim')
def trim(value):
    return value.strip()
