"""
ASGI config for deliveryapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path
from pages import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'deliveryapp.settings')

application = get_asgi_application()

ws_pattern = [
   path("ws/customer", consumers.OrderStatus),
]

application = ProtocolTypeRouter({
   'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(ws_pattern)))
})
