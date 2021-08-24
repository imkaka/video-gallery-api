from django.contrib import admin

# python/django imports
from .models import Video


@admin.register(Video)
class FlexiPassAdmin(admin.ModelAdmin):
    pass
