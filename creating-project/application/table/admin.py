from django.contrib import admin
from .models import Table, Path

# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    pass


@admin.register(Path)
class PathAdmin(admin.ModelAdmin):
    pass