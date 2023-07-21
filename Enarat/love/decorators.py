from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from love.models import Gallery

def permission_access(view_func):
    def wrapper(request,albumName, *args, **kwargs):
        # Add your custom logic here
        album = Gallery.objects.get(title = albumName)
        perm = False
        if request.user.groups.filter(name ='admin').count() > 0:
            perm = True
        if (request.user in album.users.all()) or perm:
            return view_func(request,albumName, *args, **kwargs)
        else:
            return HttpResponseForbidden("You don't have permission to access this page.")
    return wrapper
def admin_access(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name='admin').count() > 0:
            return view_func(request, *args,**kwargs)
        else:
            return redirect('profile')
    return wrapper