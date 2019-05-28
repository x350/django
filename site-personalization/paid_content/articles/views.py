from django.shortcuts import render, render_to_response
from .models import Article, Profile
from .forms import InputName
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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

    if request.user.is_authenticated:
        context['article'] = article
        return render(request, 'article.html', context)
    else:
            return render(request, 'error.html')



def sell_kidney(request):
    context = {}
    if request.method == 'GET':
        context['form'] = InputName()
        return render(request, 'paid.html', context)
    elif request.method == 'POST':
        form = InputName(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Profile.objects.create(name= User.objects.get(username=user), vip=True)
            return render(request, 'congratulations.html')
        else:
            return render(request, 'error.html', {'form': form.errors})