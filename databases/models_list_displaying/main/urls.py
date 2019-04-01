"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

import books.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books.views.BookListView.as_view(), name='book_view'),
    url(r'^book/(?P<pk>\d+$)', books.views.BookDetailView.as_view(), name='book-detail'),
    url(r'^books/(?P<stub>\d{4}-\d{2}-\d{2}$)', books.views.BookDateView.as_view(), name='book-date'),
]
