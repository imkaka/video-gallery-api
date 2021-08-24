# python imports
import logging

# django/rest_framework imports
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination

# project level import
from libs.pagination import CursorSetPagination
from libs.constants import BAD_REQUEST, BAD_ACTION
from libs.exceptions import ParseException

# app level imports
from .models import Video
from .serializers import (
    VideoSearchRequestSerializer,
    VideoResponseSerializer,
)
from .services import VideoService

logger = logging.getLogger('api')


class VideoGalleryViewSet(GenericViewSet):
    """
    Generic viewset to for interacting with video gallery.
    APIs does not support auth for simplicity.
    we can plug in DRF default Token auth eaasily.
    """

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    pagination_class = CursorSetPagination

    serializers = {
        'search': VideoSearchRequestSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializers[self.action]
        except Exception as e:
            raise ParseException(BAD_ACTION)

    def get_queryset(self):
        return Video.objects.all()

    def list(self, request, *args, **kwargs):
        """
        List API for sending all videos.
        """
        videos_queryset = VideoService.get_videos()
        page = self.paginate_queryset(videos_queryset)

        if page:
            response = VideoResponseSerializer(page, many=True).data
            return self.get_paginated_response(response)

        return Response(VideoResponseSerializer(videos_queryset, many=True).data)

    @action(methods=['get'], detail=False, url_path='search')
    def search(self, request, *args, **kwargs):
        """
        Search the videos based on query string.
        """
        logger.info(
            f'VideoGalleryViewSet : search for - {request.query_params}'
        )
        serializer = self.get_serializer(data=request.query_params)
        if serializer.is_valid() is False:
            raise ParseException(BAD_REQUEST, errors=serializer.errors)

        videos_queryset = VideoService.search_videos(q=serializer.validated_data['q'])
        page = self.paginate_queryset(videos_queryset)

        if page:
            response = VideoResponseSerializer(page, many=True).data
            return self.get_paginated_response(response)

        return Response(VideoResponseSerializer(videos_queryset, many=True).data)
