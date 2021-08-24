from celery import shared_task
from celery.utils.log import get_task_logger

from api.celery import app as celery_app

from .services import VideoService


logger = get_task_logger(__name__)


@shared_task
def fetch_videos_from_youtube():
    logger.info("Running fetch_videos_from_youtube")

    VideoService.fetch_store_videos()
