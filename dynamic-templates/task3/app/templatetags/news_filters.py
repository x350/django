from django import template
from datetime import datetime, timedelta
import time

register = template.Library()

@register.filter
def format_date(value):
    t_v = int(value.split(',')[0])
    post_time = time.gmtime(t_v)
    y = time.strftime('%Y-%m-%d %H:%M:%S', post_time)
    format_time = '%Y-%m-%d %H:%M:%S'
    print(y)
    date_since = datetime.strptime(y, format_time)
    c = datetime.now() - date_since
    delta_seconds = c.seconds
    delta_days = c.days

    if (delta_seconds < 60 * 10):
        return 'только что'
    elif (delta_days < 1):
        return str(delta_seconds // (24 * 60 * 60)) + 'часов назад'
    else:
        return  time.strftime('%Y-%m-%d', post_time)



# необходимо добавить фильтр для поля `score`


@register.filter
def format_num_comments(value):
    # Ваш код
    return value



