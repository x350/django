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
    if not article.paid:
        context['article'] = article
        return render(request, 'article.html', context)

    access = request.session.get('access', 0)
    if access:
        user = Profile.objects.get(pk=access)
        if user.vip:
            context['article'] = article
            return render(request, 'article.html', context)
        else:
            return render(request, 'error.html')
    else:
        return render(request, 'error.html')


def sell_kidney(request):
    context = {}
    if request.method == 'GET':
        context['form'] = InputName()
        return render(request, 'paid.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        new_profile = Profile.objects.create(name=name, vip=True)
        request.session['access'] = new_profile.pk
        return render(request, 'congratulations.html')
