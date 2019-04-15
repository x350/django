from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    from_landing = request.GET.get('from-landing')
    print(from_landing)
    counter_click[from_landing] += 1
    return render_to_response('index.html')


def landing(request):    
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    ab_test_arg = request.GET.get('ab-test-arg')
    counter_show[ab_test_arg] += 1
    if ab_test_arg == 'test':
        return render_to_response('landing_alternate.html')
    if ab_test_arg == 'original':
        return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        text_conv = round(counter_click['test'] / counter_show['test'], 1)
    except ZeroDivisionError:
        text_conv = 'no views'

    try:
        orig_conv = round(counter_click['original'] / counter_show['original'], 1)
    except ZeroDivisionError:
        orig_conv = 'no views'

    return render_to_response('stats.html', context={
        'test_conversion': text_conv,
        'original_conversion': orig_conv,
    })
