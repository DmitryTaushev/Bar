from django import template

register = template.Library()

@register.filter()
def drink_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/dummydog.jpg'