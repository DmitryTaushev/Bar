from django import template

register = template.Library()


@register.filter()
def category_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/dummydog.jpg'


@register.filter()
def user_media(val):
    if val:
        return f'/media/{val}'
    return '/static/inkognito.jfif'

@register.filter()
def drink_media(val):
    if val:
        return fr'/media/{val}'
    return '/static/dummydog.jpg'
