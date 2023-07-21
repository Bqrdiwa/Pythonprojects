from django.shortcuts import render
from Stogit.models import Stogit

# Create your views here.
def Main(request):
    context = {}
    return render(request, 'main/main.html', context)

def Profile(request):
    context = {}
    return render(request, 'main/profile.html', context)
def Games(request):
    context = {}
    
    games = []
        
    # Installed every block is a installed app

    # block-1 Stogit
    games.append(Stogit.objects.all().first())



    context['games'] = games
    print(games)
    return render(request,'main/games.html', context)

def test(request):
    return render(request,'main/test.html',{'title':'Test'})