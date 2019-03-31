from django.views import generic
from django.conf import settings
import os
import json
from .models import Book

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #

    #
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #
    #     return context

class BookDetailView(generic.DetailView):
    model = Book