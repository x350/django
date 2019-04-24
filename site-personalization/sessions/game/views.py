from django.shortcuts import render
from .forms import InputNumber
from .models import Player, Game,PlayerGameInfo
import string
import random
N = 20


def show_home(request):
    context = {}
    context['form'] = InputNumber()
    attempt_number = request.GET.get('number')
    key = request.session.get('key', 0)

    if not attempt_number:
        player = None
        if not key:
            key = random_key(N)
            request.session['key'] = key
            player = Player.objects.create(session_id=key)
        else:
            player = Player.objects.filter(session_id=key)

        game_wait = Game.objects.filter(wait=True)
        if not game_wait:
            game_id = random_key(N)
            number = random.randint(1, 10)
            game = Game.objects.create(game_id=game_id, number=number, wait=True)
            PlayerGameInfo.objects.create(game=game, player=player)
            context['number'] = number
            return render(request, 'start.html', context)
        else:
            player.is_attempt = True
            player.save()
            game_wait[0].wait = False
            game_wait[0].save()
            PlayerGameInfo.objects.create(game=game_wait[0], player=player)
            return render(request, 'home.html', context)

    if not key:
        return render(request, 'error.html')

    player = Player.objects.filter(session_id=key)
    current_game = Game.objects.all().order_by('-id')[0]
    current_number = current_game.number

    if player.is_attempt:
        current_game.attempt_count += 1
        current_game.save()
        message = ''
        if current_number == attempt_number:
            message = f'Вы угадали число, всего попыток {current_game.attempt_count}'
        elif current_number < attempt_number:
            message = f'Загаданное число меньше {attempt_number}'
        else:
            message = f'Загаданное число больше {attempt_number}'
        context['message'] = message
        return render(request, 'base.html', context)
    else:
        message = f'Ваше число угадывают, число попыток {current_game.attempt_count}'
        context['message'] = message
        context['form'] = ''
        return render(request, 'base.html', context)


def random_key(N):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=N))