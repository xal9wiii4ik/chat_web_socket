import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_ws.settings')
app = Celery('room')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
