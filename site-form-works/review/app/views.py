from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Product, Review
from .forms import ReviewForm
from django.shortcuts import render


class ProductsList(ListView):
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


def viewDetail(request, **kwargs):
    template = 'app/product_detail.html'
    model_product = Product
    model_review = Review
    context = {}
    context['form'] = ReviewForm()
    product = model_product.objects.get(pk=kwargs['pk'])
    context['object'] = product
    # context['reviews'] = model_review.objects.select_related(model_product)
    # print(context['reviews'])
    print(request.method)

    return render(request, template, context)




# class ProductView(DetailView):
#     model_product = Product
#     model_review = Review
#     template_name = 'app/product_detail.html'

    # def get_queryset(self, **kwargs):
    #     context = {}
    #     context['form'] = ReviewForm()
    #     print(self.kwargs['pk'])
    #     product = self.model_product.objects.get(pk=self.kwargs['pk'])
    #     context['object'] = product
    #     # context['reviews'] = self.model_review.objects.select_related(self.model_product)
    #     print(context)
    #     return context

#
    # def get_context_data(self, request, **kwargs):
    #     context = super(ProductView, self).get_context_data(**kwargs)
    #     context['form'] = ReviewForm()
    #     product =  self.model_product.objects.get(pk=kwargs['pk'])
    #     context['object'] = product
    #     # context['reviews'] = self.model_review.objects.select_related(self.model_product)
    #     return context
#
#
#     def get(self, request, **kwargs):
#         context = super(ProductView, self).get_context_data(self, **kwargs)
#         print('--------------------------------', context)
#         return  render(request=request, template_name=self.template_name, context=context )
#

#
#
#     # def post(self, request, *args, **kwargs):
#     #     pass
#     #
#     # def get_queryset(self,   *args, **kwargs):
#     #     print(self.kwargs)
#     #     queryset = {}
#     #     queryset['form'] = ReviewForm()
#     #     queryset['object'] = self.model_product.objects.get(pk=1)
#     #   # value = request.GET.get('pk')
#     #     queryset['reviews'] = self.model_review.objects.all()
#     #     return queryset
#
