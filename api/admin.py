from django.contrib import admin
from .models import Advert


class AdvertAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'photo', 'price')


admin.site.register(Advert, AdvertAdmin)