from django.urls import path
from .views import Home, Album, AlbumView, Login, AlbumADD, App, Profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',Home,name='love-home'),
    path('album/', Album, name='love-album'),
    path('albumADD/', AlbumADD, name='love-album'),
    path('album/<str:albumName>', AlbumView, name='love-album-view'),
    path('login/', Login, name='login'),
    path('app/', App, name='app'),
    path('profile/', Profile, name = 'profile')
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)