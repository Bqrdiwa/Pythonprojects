"""
ASGI config for boardgame project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
import Stogit.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boardgame.settings')


application = ProtocolTypeRouter(
    {
        'http':get_asgi_application(),
        'websocket':AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(
                Stogit.routing.websocket_urlpatterns
            ))
        )
    }
)
