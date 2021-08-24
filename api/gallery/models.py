from django.db import models

from libs.models import TimeStampedModel


class Video(TimeStampedModel):
    """
    Respresenting video data and metadata.
    """
    YOUTUBE = 'youtube'
    TIKTOK = 'tiktok'
    INSTA_REEL = 'insta_reel'
    VIDEO_SOURCE = [
        (YOUTUBE, 'Youtube'),
        (TIKTOK, 'Tiktok'),
        (INSTA_REEL, 'Instagram Reels'),
    ]
    video_source = models.CharField(max_length=16, choices=VIDEO_SOURCE, default=YOUTUBE)

    title = models.CharField(max_length=256)
    description = models.TextField()
    published_at = models.DateTimeField(db_index=True)

    """
    Example:
    {
        "default": {
            "height": 90,
            "url": "https://i.ytimg.com/vi/jvwGn-LmfwE/default.jpg",
            "width": 120
        },
        "high": {
            "height": 360,
            "url": "https://i.ytimg.com/vi/jvwGn-LmfwE/hqdefault.jpg",
            "width": 480
        },
        "medium": {
            "height": 180,
            "url": "https://i.ytimg.com/vi/jvwGn-LmfwE/mqdefault.jpg",
            "width": 320
    }
    """
    thumbnails = models.JSONField(default=dict)

    class Meta:
        app_label = 'gallery'
        db_table = 'api_video'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return f"Video({self.title})"
