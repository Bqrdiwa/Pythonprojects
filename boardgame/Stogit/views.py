from django.shortcuts import render
from .models import StogitGame, StogitPlayer, HostForm, StogitStatus, StogitStats
from django.http import JsonResponse
from .decorators import lobby_join_permission
# Create your views here.
def Main(request):
    context = {'title':'Main'}
    return render(request, 'Stogit/main.html',context)

def Tutorial(request):
    context = {'title':'Tutorial'}
    return render(request, 'Stogit/tutorial.html',context)

def Lobbys(request):
    context = {'title':'Lobbys'}
    context['lobbys'] = StogitGame.objects.all()
    return render(request, 'Stogit/lobbys.html', context)

@lobby_join_permission
def Lobby(request, lobbyName):
    context = {'title':lobbyName}
    lobbyR = StogitGame.objects.get(lobbyName=lobbyName)
    context['players'] = StogitPlayer.objects.all().filter(gameRelated = lobbyR)
    player ,created = StogitPlayer.objects.get_or_create(userRelated = request.user, gameRelated = lobbyR)
    if created:
        player.random_color()
    player.connected = 'True'
    player.save()
    print(player.role)
    context['ply'] = player
    context['game']= lobbyR
    return render(request, 'Stogit/lobby.html', context)

def Game(request, lobbyName):
    context = {'title':lobbyName}
    gameR = StogitGame.objects.get(lobbyName=lobbyName)
    player = StogitPlayer.objects.get(userRelated = request.user)
    
    if request.method == 'POST':
        DATA = request.POST
        command  = DATA['command']
        if command == 'initiate':
            gameR.Initiate()
        return JsonResponse(context)
    else:
        Stats = StogitStats.objects.get_or_create(player = request.user)
        status = StogitStatus.objects.get(player = player)
        context['players'] = StogitGame.players
        context['game'] = gameR
        context['cards'] = status.cards
        context['ply'] = player
    
        return render(request, 'Stogit/game.html', context)

def Host(request):
    context = {'title':'Stogit - Host'}
    if request.method == 'POST':
        form  = HostForm(request.POST)
        if form.is_valid():
            context['errors'] = 'None'
            game = StogitGame.objects.create(lobbyName = request.POST['lobbyName'],
                                      count = request.POST['count'],
                                      points = request.POST['points'],
                                      mode = request.POST['mode']
                                      )
            player = StogitPlayer.objects.create(userRelated = request.user,
                                        gameRelated = game,
                                        role ='ST'
                                        )
            player.random_color()
        else:
            errors = form.errors
            context['errors'] = errors
        return JsonResponse(context)
    else:
        form = HostForm()
        context['form'] = form
        return render(request, 'Stogit/host.html', context)