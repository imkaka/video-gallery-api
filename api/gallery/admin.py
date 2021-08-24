# django and rest_framework imports
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html

# project level imports
from libs.admin import AbstractBaseModelAdmin

# app level imports
from .models import Video
@admin.register(Video)
class VideoAdmin(AbstractBaseModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'published_at',
        'thumbnail',
        'created_at',
    )
    list_display_links = ('id',)

    # This search is very inefficient
    # (keeping it until we have we have small amout of data)
    search_fields = ('title', 'description')
    list_filter = ('video_source',)

    def thumbnail(self, obj):
        if obj.thumbnails:
            link = mark_safe(
                f'<a target="_blank" rel="noopener noreferrer" href={obj.thumbnails["default"]["url"]}>Defalut Thumbnail</a>'
            )
        else:
            link = None
        return link

    def thumbnail_default(self, obj):
        if obj.thumbnails:
            link = format_html(
                f'''<a target="_blank" rel="noopener noreferrer"
                    href={obj.thumbnails['default']['url']}><img src="{obj.thumbnails['default']['url']}"
                    width="250" height="250"/></a>
                '''
            )
        else:
            link = None
        return link

    def get_fieldsets(self, request, obj=None):
        fieldsets = (
            (
                'Thumbnail Image',
                {'fields': ('thumbnail_default', )},
            ),
            (
                'Basic Video Attributes',
                {
                    'fields': (
                        'id',
                        'title',
                        'description',
                        'published_at',
                        'thumbnail',
                        'created_at',
                    )
                },
            ),
        )
        return fieldsets
