from django import template

register = template.Library()

@register.filter
def background(value):
    value = float(value)
    if value < 0:
        return 'green'
    if (value >= 0)  and (value < 1):
        return 'white'
    elif (value >= 1) and (value < 2):
        return '#FF7373'
    elif (value >= 2) and (value < 5):
        return '#FF4040'
    else:
        return '#A60000'


