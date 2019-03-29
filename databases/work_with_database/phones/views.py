from django.shortcuts import render
from .models import Phone

def show_catalog(request):
    phone = Phone.objects.all()
    sort = request.GET.get("sort", "")




    context = {'phone': phone}
    return render(
        request,
        'catalog.html',
        context
    )


def show_product(request, slug):
    return render(
        request,
        'product.html',
    )
