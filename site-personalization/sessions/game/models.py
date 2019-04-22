from django.db import models


class Player(models.Model):
    session_id = models.CharField(max_length=512)

# #
class Game(models.Model):
    game_id = models.CharField(max_length=512)
    number = models.IntegerField(verbose_name='Число')
    players = models.ManyToManyField(Player, through='PlayerGameInfo')
    wait = models.BooleanField(verbose_name='Ждем второго', default=False)


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    attept = models.IntegerField(verbose_name='Число попыток', default=0)
    player_attempt_id = models.CharField(max_length=512, null=True)




