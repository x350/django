from django.views.generic import ListView

from .models import Article

# from django.db.models import QuerySet
# from django.core.exceptions import ImproperlyConfigured


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_queryset(self):
        queryset = self.model.objects.select_related('author').only('image', 'title', 'text', 'author', 'genre')
        print(queryset.values())
        return queryset




