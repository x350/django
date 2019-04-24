from django.shortcuts import render, render_to_response
from .models import Article, Profile
from .forms import InputName


def show_articles(request):
    context = {}
    context['articles'] = Article.objects.all().only('id', 'title')

    return render(
        request,
        'articles.html',
        context
    )


def show_article(request, id):
    context = {}
    article = Article.objects.get(pk=id)
    access = request.session.get('access', 0)
    if not article.paid or access == 'have':
        context['article'] = article
    else:
        article.text = ''
        context['article'] = article

    return render(
        request,
        'article.html',
        context
    )


def sell_kidney(request):
    name = request.GET.get('name')
    context = {}
    if not name:
        context['form'] = InputName()
        return render(request, 'paid.html', context)
    else:
        request.session['access'] = 'have'
        Profile.objects.create(name=name, vip=True)
        return render(request, 'congratulations.html')

