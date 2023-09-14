import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class QueueConsumer(WebsocketConsumer):
    def connect(self):
        self.queue_id = self.scope["url_route"]["kwargs"]["queue_id"]
        self.room_group_name = f"queue_{self.queue_id}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def queue_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps(message))
