from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'review_count')
    ordering = ['pk']


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    ordering = ['-pk']


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)

