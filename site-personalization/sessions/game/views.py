from django.shortcuts import render
from .forms import InputNumber
from .models import Player, Game,PlayerGameInfo
import string, random
N = 20



def show_home(request):
    key = request.session.get('key', 0)
    if not key:
        key = random_key(N)
        request.session['key'] = key
        game_id = random_key(N)
        game_wait = Game.objects.filter(wait=True)
        print(game_wait)

         # создание игры
        if not game_wait.wait:
            player = Player.objects.create(session_id=key, game_id=game_id)
            game = Game.objects.create(game_id=game_id, attempt=0, players=player, number=random.randint(1,10), wait=True)
            # chech_wait.wait = True
            # chech_wait.save()
        else:
            player_2 = Player.objects.create(session_id=key, game_id=game_wait.game_id)
            game_wait.add(player_2)
            game_wait.wait = False
            game_wait.save()


    else:
        pass



    context = {}
    context['form'] = InputNumber()
    current_game = Game.objects.all().order_by('-id')[0]
    context['number'] = current_game.number
    return render(request, 'start.html', context)


def random_key(N):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=N))