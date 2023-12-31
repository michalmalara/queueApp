import json
import logging

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class QueueConsumer(WebsocketConsumer):
    def connect(self):
        self.queue_id = self.scope["url_route"]["kwargs"]["queue_id"]
        self.room_group_name = f"queue_{self.queue_id}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()
        print(f"Consumer connected to queue {self.queue_id}")
        self.send(text_data=json.dumps({"message": "Connected"}))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def queue_message(self, event):
        message = event["message"]

        self.send(text_data=json.dumps(message))
