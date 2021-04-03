import json
import requests

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.urls import reverse


def log_in(request, data: dict) -> dict:
    """Check password and return tokens or false"""

    try:
        user = get_user_model().objects.get(username=data['username'])
        if check_password(data['password'], user.password):
            url = _get_web_url(
                is_secure=request.is_secure(),
                host=request.get_host(),
                url=reverse('token')
            )
            response = requests.post(url=url, json={
                'password': data['password'],
                'username': user.username
            })
            data = json.loads(response._content.decode('utf-8'))
            data.update({'user_id': user.id})
            return data
        return {'error': 'Invalid password'}
    except Exception:
        return {'error': 'User does not exist'}


def _get_web_url(is_secure: bool, host: str, url: str) -> str:
    """Получение ссылки"""

    protocol = 'https://' if is_secure else 'http://'
    web_url = protocol + host
    return web_url + url
