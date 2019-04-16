from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'
    # form_class =

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset



class ProductView(DetailView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form_class = ReviewForm
        print(context)
        # return context

    def post(self, request, *args, **kwargs):
        pass

