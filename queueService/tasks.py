import logging

import celery

from .models import Queue
from .notification_provider.websockets_notification_provider import WebsocketsNotificationProvider
from .utils import get_other_queues_info

notification_provider = WebsocketsNotificationProvider()


@celery.shared_task
def update_queues_info():
    queues = Queue.objects.filter(
        datetime_completed__isnull=True
    )

    for queue in queues:
        notification_provider.update_queue_info(get_other_queues_info(queue))

    logging.info("Queues info updated")
