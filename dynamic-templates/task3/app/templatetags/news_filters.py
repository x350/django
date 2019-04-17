from django import template
from datetime import datetime, timedelta
import time

register = template.Library()


@register.filter
def format_date(value):
    t_v = int(value)
    post_time = time.gmtime(t_v)
    y = time.strftime('%Y-%m-%d %H:%M:%S', post_time)
    format_time = '%Y-%m-%d %H:%M:%S'
    date_since = datetime.strptime(y, format_time)
    c = datetime.now() - date_since
    delta_seconds = c.seconds
    delta_days = c.days

    if delta_seconds < 60 * 10:
        return 'только что'
    elif delta_days < 1:
        return str(delta_seconds // (60 * 60)) + ' часов назад'
    else:
        return time.strftime('%Y-%m-%d', post_time)


# необходимо добавить фильтр для поля `score`
@register.filter
def format_rating(value):
    # Ваш код
    rating = int(value)
    if rating < -5:
        return 'все плохо'
    elif (rating >= -5) and (rating <= 5):
        return 'нейтрально'
    elif rating > 5:
        return 'хорошо'
    else:
        return value


@register.filter
def format_num_comments(value):
    # Ваш код
    num_comm = int(value)
    if num_comm == 0:
        return 'Оставте комментарий'
    elif (num_comm > 0) and (num_comm <= 50):
        return str(num_comm)
    elif num_comm > 50:
        return '50+'
    else:
        return value


@register.filter
def format_selftext(text, count):
    if len(text) > (count * 2 + 1):
        array_word = text.split(' ')
        return ' ... '.join([' '.join(array_word[:count]), ' '.join(array_word[-count:])])
    else:
        return text
