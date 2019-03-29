from django.contrib import admin
from .models import Phone
# Register your models here.

# first variant
@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = (
        'brend', 'model_phone', 'os_phone', 'display_size', 'storage_memory',
        'fm_tuner', 'nfc', 'cpu_frequency', 'color', 'camera_mp',
    )

# second variant
# class PhoneAdmin(admin.ModelAdmin):
#     list_display = (
#         'brend', 'model_phone', 'os_phone', 'display_size', 'storage_memory',
#         'fm_tuner', 'nfc', 'cpu_frequency', 'color', 'camera_mp',
#     )
#
# admin.site.register(Phone, PhoneAdmin)