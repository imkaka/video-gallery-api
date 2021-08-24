import os
import logging

from django.conf import settings

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


logger = logging.getLogger('api')


class YoutubeClient:

    @classmethod
    def search(
        cls,
        published_after: str,
        key: str,
        q: str = settings.YOUTUBE_CONFIG['SEARCH_KEYWORD'],
        entity: str='video',
        order: str ='date'
    ):
        """
        """
        try:
            with build('youtube', 'v3', developerKey=key) as youtube:
                request = youtube.search().list(
                    part='snippet',
                    q=q,
                    publishedAfter=published_after,
                    type=entity,
                    order=order,
                    maxResults=50
                )
                return request.execute()
        except Exception as e:
            logger.info(f'YoutubeClient error while fetching videos {e}')
            return None  # Generic Exception will also handle quota over error.
