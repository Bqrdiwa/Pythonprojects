from django.urls import path
from .views import Main, Tutorial, Lobbys, Lobby, Game, Host

urlpatterns = [
    path('', Main, name='stogit-main'),
    path('Tutorial/', Tutorial, name='stogit-tutorial'),
    path('Lobbys/', Lobbys, name='stogit-lobbys'),
    path('Lobbys/<lobbyName>', Lobby, name='stogit-lobby'),
    path('Games/<lobbyName>', Game, name='stogit-game'),
    path('Host/',Host, name='stogit-host')
]