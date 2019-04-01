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
    template_name = 'books/book_date.html'
    model = Book
    paginate_by = 1

    def get_queryset(self):
        print(self.kwargs)
        # qs = super().get_queryset()

        return Book.objects.order_by('pub_date')
