# python level imports
import logging

# django/rest-framework imports
from django.utils import timezone
from django.db.models import Q

# project level imports
from libs.clients.youtube import YoutubeClient

# app level imports
from .models import Video
from .constants import PUBLISHED_AFTER_MINUTES

logger = logging.getLogger('api')


class VideoService:
    """
    Service to handle all Video related stuff.
    """

    def __init__(self, video: Video) -> None:
        self.video = video

    @classmethod
    def get_videos(cls):
        return Video.objects.all().order_by('-published_at')

    @classmethod
    def search_videos(cls, q: str):
        return Video.objects.filter(Q(title__contains=q) | Q(description__contains=q))

    @classmethod
    def fetch_store_videos(cls) -> None:
        """
        Fetch the videos for defined keyword & store it in DB.
        """
        published_after = (timezone.now() - timezone.timedelta(minutes=PUBLISHED_AFTER_MINUTES)).isoformat()
        video_data = YoutubeClient.search(published_after)

        if not video_data:
            return

        videos = []
        for video in video_data['items']:
            snippet = video['snippet']
            videos.append(
                Video(
                    title=snippet['title'],
                    description=snippet['description'],
                    published_at=snippet['publishedAt'],
                    thumbnails=snippet['thumbnails'],
                )
            )

        # Record this to DB in bulk
        Video.objects.bulk_create(videos)
