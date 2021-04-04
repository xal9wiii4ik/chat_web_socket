import json

from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer
from chat.models import Room, Message
from chat.tasks import add_message


def send_message(self, name: str):
    """ Sending all messages that was before """

    room = Room.objects.get(name=name)
    messages = Message.objects.filter(room=room)
    for message in messages:
        self.send(text_data=json.dumps({
            'message': message.text
        }))


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.chat_type = self.scope['url_route']['kwargs']['chat_type']
        self.room_group_name = f'chat_{self.room_name}s'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        if self.chat_type == 'constant':
            self.user_id = self.scope['user']
            send_message(self=self, name=self.room_name)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': text_data_json['message'],
                'username': text_data_json['username']
            }
        )

    def chat_message(self, event):
        data = {
            'message': event['message'],
            'username': event['username']
        }

        if self.chat_type == 'constant':
            add_message.delay(user_id=self.user_id, message=data['message'], room_name=self.room_name)
        self.send(text_data=json.dumps(data))
