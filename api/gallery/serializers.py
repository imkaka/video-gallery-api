# django/rest-framework imports
from rest_framework import serializers

# app level imports
from .models import Video


class VideoSearchRequestSerializer(serializers.Serializer):
    """
    """
    q = serializers.CharField(required=True)


class VideoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            'id',
            'video_source',
            'title',
            'description',
            'published_at',
            'created_at',
            'thumbnails',
        )
        read_only_fields = fields
