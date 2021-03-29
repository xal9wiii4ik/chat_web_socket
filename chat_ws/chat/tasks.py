import json

from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from chat.models import Room, Message
from chat_ws import settings
from chat_ws.celery import app


@app.task
def send_invited_email(web_url: str, room_id: id, user_id: int):
    """ Send email with invited message to the chat """

    user = get_user_model().objects.get(id=user_id)
    room = Room.objects.get(id=room_id)
    url = web_url + f'/chat/{room.name}/constant/'
    send_mail(subject='Invited message',
              message=f'you have received an invitation to the chat.\n Please follow this link: \n {url}',
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[user.email],
              fail_silently=False)


@app.task
def add_message(user_id: int, message: str, room_name: str):
    """ Add message to database """

    user = get_user_model().objects.get(id=user_id)
    room = Room.objects.get(name=room_name)
    Message.objects.create(owner=user, room=room, text=message)


@app.task
def send_messages(self, room_name: str):
    """ Sending all messages that was before """

    room = Room.objects.get(name=room_name)
    messages = Message.objects.filter(room=room)
    for message in messages:
        self.send(text_data=json.dumps({
            'message': message.text
        }))
