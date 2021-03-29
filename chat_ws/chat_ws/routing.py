from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import chat.routing


application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    'websocket': JWTAuthMiddlewareStack(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})