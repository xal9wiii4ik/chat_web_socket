from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

import chat.routing
from chat.jwt_middleware import JWTTokenAuthMiddleware


application = ProtocolTypeRouter({

    "http": get_asgi_application(),
    'websocket': JWTTokenAuthMiddleware(
        URLRouter(chat.routing.websocket_urlpatterns)
    ),
})