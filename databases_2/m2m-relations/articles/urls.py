from django.urls import path

# from articles.views import ArticleListView
from articles.views import articleTags

urlpatterns = [
    # path('', ArticleListView.as_view()),
    path('', articleTags),
]
