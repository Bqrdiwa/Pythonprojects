from django.shortcuts import render, redirect
from .models import Gallery,Log, Another
from django.http import JsonResponse
from .models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import permission_access, admin_access
# Create your views here.
@login_required
@admin_access
def Home(request):
    context ={}
    if request.method =='POST':
        data  = request.POST
        op = data['another']
        context['created'] = 'NO!'
        _, created = Another.objects.get_or_create(anotherOp = op, sender = request.user)
        if created:
            context['created'] = 'OK!'
        return JsonResponse(context)
    else:
        if(request.user.username != 'Bqrdiwa'):
            Log.objects.create(user = request.user,where = 'Home')
        return render(request, 'home.html', context = context)

@login_required
def Album(request):
    context = {}
    if request.method == 'POST':
        DATA = request.POST
        action = DATA['action']
        pk = DATA['album-pk']
        album = Gallery.objects.get(pk = pk)

        if action == 'DEL':
            album.delete()
        elif action == 'EDIT':
            files = request.FILES

            if 'image' in files.keys():
                album.thumbnail = files['image']
            album.title = DATA['title']
            album.save()
        return JsonResponse(context)
    else:
        perm = False
        if request.user.groups.filter(name='admin').count() > 0:
            perm = True
        context['perm']= perm
        context['albums'] = Gallery.objects.all()
        if(request.user.username != 'Bqrdiwa'):
            Log.objects.create(user = request.user,where = 'Albums')
        return render(request, 'album.html', context = context)

@login_required
@permission_access
def AlbumView(request, albumName):
    context = {}

    album = Gallery.objects.get(title = albumName)
    context['album'] = album
    perm = 'False'
    if request.user.groups.filter(name='admin').count() > 0:
        perm = 'True'
    context['perm']= perm
    if(request.user.username != 'Bqrdiwa'):
        Log.objects.create(user = request.user,where = 'Album-View: '+albumName)
    return render(request, 'album_view.html', context = context)

def Login(request):
    context = {}
    if request.method =='POST':
        perm_usernames = ['تران', 'taran','shambayati', 'شامبیاتی','بردیا','bardia']
        data = request.POST
        username = data['username']
        password = data['password']
        context['ERR'] = 'None'
        if username == '' or password == '':
            if username == '':
                context['ERR'] = 'یه یوزرنیم بزن نمیشه خالی باشه'
            else:
                context['ERR'] =  'یه پسورد بزن اسکل'
        try:
            User.objects.get(username =username)
            user = authenticate(username= username, password=password)
            if user != None:
                login(request, user)
                context['ERR'] = 'Logined'
            else:
                context['ERR'] = f'پسوردتو درست وارد کردی؟{username} پسوردش این نبود'
        except:
            pass
        if context['ERR']  == 'None':
            user = User.objects.create_user(username =username, password=password)
            for i in perm_usernames:
                username = username.lower()
                if i in username:
                    adminG= Group.objects.get(name='admin')
                    user.groups.add(adminG)
            login(request, user)
        
        return JsonResponse(context)
    else:
        return render(request, 'login.html', context = context)
@login_required
@admin_access
def AlbumADD(request):
    context = {}
    if request.method =='POST':
        files = request.FILES
        data = request.POST
        if 'image' in files.keys():
            Gallery.objects.create(title = data['title'], thumbnail= files['image'])
        else:
            Gallery.objects.create(title = data['title'])
        return JsonResponse(context)
    else:
        if(request.user.username != 'Bqrdiwa'):
            Log.objects.create(user = request.user,where = 'AlbumADD')
    return render(request, 'albumADD.html', context)

@login_required
def App(request):
    context = {}
    return render(request, 'app.html', context)

def Profile(request):
    context = {}
    if(request.user.username != 'Bqrdiwa'):
        Log.objects.create(user = request.user,where = 'Profile')
    return render(request, 'profile.html', context)