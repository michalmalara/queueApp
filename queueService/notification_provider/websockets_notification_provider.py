from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from queueService.notification_provider.notification_provider_abstract import NotificationProviderAbstract


class WebsocketsNotificationProvider(NotificationProviderAbstract):
    def __init__(self):
        self.__channel_layer = get_channel_layer()

    def update_queue_info(self, queue_data: dict) -> None:
        async_to_sync(self.__channel_layer.group_send)(
            f"queue_{queue_data.get('id')}",
            {
                "type": "queue_message",
                "message": queue_data
            }
        )
