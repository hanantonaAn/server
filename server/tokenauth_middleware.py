from channels.db import database_sync_to_async
from django.contrib.auth.models import AnonymousUser
from channels.middleware import BaseMiddleware
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken

@database_sync_to_async
def get_user(token_key):
    try:
        # Попытка получить токен по ключу
        token = AccessToken(token_key)
        # Проверка валидности токена
        token.verify()  # Используйте verify() для проверки валидности токена
        # Получение пользователя по токену
        user_id = token.payload.get('user_id')
        print("______USER________")
        print(user_id)
        if user_id is not None:
            return user_id  # Возвращаем ID пользователя, а не сам объект User
    except InvalidToken:
        # Возвращаем анонимного пользователя, если токен недействителен
        return AnonymousUser()

class TokenAuthMiddleware(BaseMiddleware):

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Извлечение токена из query_string
        token_key = scope['query_string'].decode().split('=')[-1]
        # Получение пользователя по токену
        scope['user'] = await get_user(token_key)
        # Передача запроса дальше по цепочке обработчиков
        return await super().__call__(scope, receive, send)
