


from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from memor.controller import routing
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({

    'http':get_asgi_application(),
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})