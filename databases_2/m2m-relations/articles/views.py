from django.views.generic import ListView

from articles.models import Article, Tags

# class ArticleListView(ListView):
#     template_name = 'articles/news.html'
#     model = Article
#     ordering = '-published_at'
#
#     def get_queryset(self):
#         queryset = self.model.objects.all().prefetch_related('tags')
#         return queryset



# так и не понял, почему пропадает tags в возвращаемом QuerySet в ArticleListView, документация и гугл не помогли
# сделал по другому
from django.shortcuts import render

def articleTags(request):
    model = Article
    queryset = model.objects.all().prefetch_related('tags')
    object_list = []
    for item in queryset:
        object_list.append({
            'title': item.title,
            'text': item.text,
            'image': item.image,
            'tags': item.tags.all()
        })
    context = {
        'object_list': object_list,
    }
    print(object_list)
    return render(request, 'articles/news.html', context)

