from django.contrib.auth import get_user_model
from django.db import close_old_connections

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import UntypedToken


from urllib.parse import parse_qs
from channels.db import database_sync_to_async
from jwt import decode as jwt_decode

from chat_ws import settings


@database_sync_to_async
def get_user(user_id: int):
    user = get_user_model().objects.get(id=user_id)
    print(type(user))
    return user


class JWTTokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        close_old_connections()
        token = parse_qs(scope['query_string'].decode('utf8'))['token'][0]

        try:
            UntypedToken(token=token)
        except (InvalidToken, TokenError) as e:
            return await self.inner(scope, receive, send)
        else:
            decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = await get_user(int(decoded_data['user_id']))
            scope['user'] = user
        return await self.inner(scope, receive, send)
