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
    id_product = pk=kwargs['pk']
    context = {}
    product = model_product.objects.get(pk=id_product)
    context['object'] = product
    context['form'] = ReviewForm()
    value_visit = []

    if request.method == 'POST':
        from_form = ReviewForm(request.POST)
        if from_form.is_valid():
            model_review.objects.create(text=from_form.data['text'], product=model_product.objects.get(pk=id_product))
            context['reviews'] = model_review.objects.filter(product=id_product)
            print(context['reviews'])
            return render(request, template, context)
    else:
        # if 'visit' in request.session:
        #     value_visit = request.session['visit']
        #     if id_product in value_visit:
        #         context['reviews'] = model_review.objects.filter(product=id_product)
        #         print(context['reviews'])
        #
        #         return render(request, template, context)
        #     else:
                context['reviews'] = model_review.objects.filter(product=id_product)
                context['form'] = ReviewForm()
                value_visit.append(id_product)
                request.session['visit'] = value_visit
                return render(request, template, context)





#
# class ProductView(DetailView):
#     model = Product
#     model_review = Review
#     form_class = ReviewForm
#     template_name = 'app/product_detail.html'
#     gueryset = model.objects.all()

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
#     def get_context_data(self, request, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form'] = ReviewForm()
#         product =  self.model.objects.get(pk=kwargs['pk'])
#         context['object'] = product
#         # context['reviews'] = self.model_review.objects.select_related(self.model_product)
#         print(context)
#         return context
# # #
# #
#     def get(self, request, **kwargs):
#         context = self.get_context_data(request, **kwargs)
#         print('--------------------------------', context)
#         return  render(request=request, template_name=self.template_name, context=context )
#
#
# #
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


