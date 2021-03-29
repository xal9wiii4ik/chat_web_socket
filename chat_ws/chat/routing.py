from django.urls import path

from .consumers import ChatConsumer


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/<str:chat_type>/', ChatConsumer.as_asgi())
]
