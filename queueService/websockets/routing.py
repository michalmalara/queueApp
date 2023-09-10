from django.urls import re_path

from queueService.websockets import consumers

websocket_urlpatterns = [
    re_path(r"ws/queue/(?P<queue_id>\w+)/$", consumers.QueueConsumer.as_asgi()),
]
