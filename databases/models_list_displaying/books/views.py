from django.views import generic
from django.conf import settings
import os
import json
from .models import Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 1



class BookDetailView(generic.DetailView):
    model = Book

class BookDateView(generic.ListView):
    # template_name = 'books/book_date.html'
    model = Book
    paginate_by = 1

    # def get_queryset(self):
    #     print(self.kwargs)
    #
    #     return Book.objects.order_by('pub_date')
    # #
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        context['book_list'] = Book.objects.filter(pub_date=self.kwargs['date'])
        return context