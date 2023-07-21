from django.urls import path 
from .cosumers import  StogitLobbyConsumer, StogitGameConsumer

websocket_urlpatterns = [
    path('ws/<str:lobbyName>/', StogitLobbyConsumer.as_asgi()),
    path('ws/Game/<str:lobbyName>/',StogitGameConsumer.as_asgi())
]
