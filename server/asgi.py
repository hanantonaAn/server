"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# application = get_asgi_application()

import os, django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from channels.routing import URLRouter, ProtocolTypeRouter
from channels.security.websocket import AllowedHostsOriginValidator  # new
from django.core.asgi import get_asgi_application
from portfolio import routing  # new
from channels.auth import AuthMiddlewareStack
from portfolio.routing import websocket_urlpatterns
from server.tokenauth_middleware import TokenAuthMiddleware



django_asgi_app = get_asgi_application()

websocket_application = AuthMiddlewareStack(
    URLRouter(
         websocket_urlpatterns
    )
)

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(  # new
        TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)))
})