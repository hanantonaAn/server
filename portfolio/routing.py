from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<int:room_name>/', consumers.EchoConsumer.as_asgi()),
]