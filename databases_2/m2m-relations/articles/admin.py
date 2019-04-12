from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tags


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            print(form.cleaned_data)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода




class TagsInLine(admin.TabularInline):
    model = Tags.articles.through
    # formset = RelationshipInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'text', 'published_at', 'image',
    )
    inlines = [
        TagsInLine,
    ]


@admin.register(Tags)
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'topic', 'is_main'
    )
    # exclude = ('articles',)
    inlines = [
        TagsInLine,
    ]