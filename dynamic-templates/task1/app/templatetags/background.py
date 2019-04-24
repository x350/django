from django import template

register = template.Library()

@register.filter
def background(value):
    color = 'white'
    if value == '':
        return color
    value = float(value)
    if value < 0:
        color = 'green'
    elif (value >= 0)  and (value < 1):
        pass
    elif (value >= 1) and (value < 2):
        color = '#FF7373'
    elif (value >= 2) and (value < 5):
        color = '#FF4040'
    else:
        color = '#A60000'
    return color


