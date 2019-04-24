from django.db import models


class Player(models.Model):
    session_id = models.CharField(max_length=512)
    is_attempt = models.BooleanField(default=False)

# #
class Game(models.Model):
    game_id = models.CharField(max_length=512)
    number = models.IntegerField(verbose_name='Число')
    players = models.ManyToManyField(Player, through='PlayerGameInfo')
    wait = models.BooleanField(verbose_name='Ждем второго', default=False)
    attempt_count = models.IntegerField(verbose_name='Число попыток', default=0)



class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)





