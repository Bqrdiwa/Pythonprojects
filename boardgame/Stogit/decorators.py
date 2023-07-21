from .models import StogitStatus,StogitGame,StogitPlayer
from django.shortcuts import redirect

def lobby_join_permission(view_func):
    def wrapper(request,lobbyName ,*args, **kwargs):
        try:
            player = StogitPlayer.objects.get(userRelated = request.user)
            StogitStatus.objects.get(player = player)
            return redirect('stogit-game',lobbyName)
        except:
            return view_func(request,lobbyName ,*args,**kwargs)
    return wrapper