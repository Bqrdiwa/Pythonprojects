
from django.urls import path
from .cosumers import LoveConsumer

websocket_urlpatterns = [
    path('ws/<str:albumName>/',LoveConsumer.as_asgi())
]