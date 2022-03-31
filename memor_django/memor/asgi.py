"""
ASGI config for raspberry project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from memor.controller import routing
from django.conf.urls import url
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'raspberry.settings')

application = ProtocolTypeRouter({
    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # # WebSocket chat handler
    # "websocket": AuthMiddlewareStack(
    #     URLRouter([
    #         url(r"^chat/admin/$", AdminChatConsumer.as_asgi()),
    #         url(r"^chat/$", PublicChatConsumer.as_asgi()),
    #     ])
    # ),
})


