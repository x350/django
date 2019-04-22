from django.contrib import admin

from .models import Profile, Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'thematic', 'text', 'paid'
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'vip'
    )
