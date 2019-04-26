from django.shortcuts import render
from .forms import InputNumber
from .models import Player, Game,PlayerGameInfo
import string
import random
N = 20


def show_home(request):
    context = {}
    context['form'] = InputNumber()
    attempt_number = int(request.GET.get('number', 0))
    key = request.session.get('key', 0)

    if not attempt_number:
        if not key:
            key = random_key(N)
            request.session['key'] = key
            player = Player.objects.create(session_id=key)
        else:
            player = Player.objects.filter(session_id=key)[0]
            if not player:
                player = Player.objects.create(session_id=key)

        game_wait = Game.objects.filter(wait=True)
        if not game_wait:
            current_game = Game.objects.filter(continue_attempt=True)
            if current_game and player.is_attempt != True:
                # current_game = Game.objects.all().order_by('-id')[0]
                message = f'Ваше число угадывают, число попыток {current_game[0].attempt_count}'
                context['message'] = message
                context['form'] = ''
                return render(request, 'home.html', context)

            player.is_attempt = False
            player.save()

            game_id = random_key(N)
            number = random.randint(1, 10)
            game = Game.objects.create(game_id=game_id, number=number, wait=True, continue_attempt=True)
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
    current_number = int(current_game.number)

    if player[0].is_attempt:
        current_game.attempt_count += 1
        current_game.save()
        message = ''
        if current_number == attempt_number:
            context['form'] = ''
            message = f'Вы угадали число, всего попыток {current_game.attempt_count}'
            player[0].is_attempt = False
            player[0].save()
            current_game.continue_attempt = False
            current_game.save()
        elif current_number < attempt_number:
            message = f'Загаданное число меньше {attempt_number}'
        else:
            message = f'Загаданное число больше {attempt_number}'
        context['message'] = message
        return render(request, 'home.html', context)
    else:
        message = f'Ваше число угадывают, число попыток {current_game.attempt_count}'
        context['message'] = message
        context['form'] = ''
        return render(request, 'home.html', context)


def random_key(N):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=N))