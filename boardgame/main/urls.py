from django.urls import path, include
from . import views as main_view

urlpatterns =[
    path('' ,main_view.Main),
    path('profile/', main_view.Profile, name='profile'),
    path('Games/', main_view.Games, name='main-games'),
    path('Stogite/', include('Stogit.urls')),
    path('test/',main_view.test)
]