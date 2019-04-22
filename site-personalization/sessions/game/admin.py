from django.contrib import admin
from .models import Player, Game,  PlayerGameInfo

class PlayerGameInfoInline(admin.TabularInline):
    model = PlayerGameInfo


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'session_id',
    )
    inlines = (PlayerGameInfoInline,)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'game_id', 'number', 'wait'
    )
    inlines = (PlayerGameInfoInline,)

