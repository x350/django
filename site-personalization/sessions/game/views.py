from django.shortcuts import render
from .forms import InputNumber
from .models import Player, Game,PlayerGameInfo
import string, random
N = 20



def show_home(request):
    context = {}
    context['form'] = InputNumber()
    key = request.session.get('key', 0)
    game_wait = Game.objects.filter(wait=True)

    if not key:
        key = random_key(N)
        request.session['key'] = key

    if not game_wait:
        player = Player.objects.create(session_id=key, is_attempt=False)
        game_id = random_key(N)
        number = random.randint(1, 10)
        game = Game.objects.create(game_id=game_id, number=number, wait=True)
        game.players.set(player)
        context['number'] = number
        return render(request, 'start.html', context)
    else:
        player_2 = Player.objects.create(session_id=key, is_attempt=True)
        print(game_wait)
        game_wait.wait = False
        game_wait.players.add(player_2)
        game_wait.save()
        return render(request, 'home.html', context)




    context = {}
    context['form'] = InputNumber()


    # current_game = Game.objects.all().order_by('-id')[0]
    # context['number'] = current_game.number
    #

    return render(request, 'start.html', context)


def random_key(N):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=N))