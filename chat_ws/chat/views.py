from rest_framework import status, renderers, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from django.shortcuts import render

from chat.models import InvitedPerson
from chat.services_views import create_room, join_chat, count_invited_persons
from chat.serializers import InvitedPersonModelSerializer
from chat.tasks import send_invited_email


class InvitedPersonModelViewSet(mixins.CreateModelMixin,
                                mixins.DestroyModelMixin,
                                GenericViewSet):
    """ View set for Invited persons """

    queryset = InvitedPerson.objects.all()
    serializer_class = InvitedPersonModelSerializer

    def create(self, request, *args, **kwargs):
        if count_invited_persons(request=request):
            protocol = 'https://' if request.is_secure() else 'http://'
            web_url = protocol + request.get_host()
            send_invited_email(web_url=web_url, room_id=request.data['room'], user_id=request.data['user'])
            return super().create(request, *args, **kwargs)
        else:
            return Response(data={'error': 'You can invite only 3 users'}, status=status.HTTP_400_BAD_REQUEST)


class RoomAPIView(APIView):
    """ API view for room """

    renderer_classes = [renderers.TemplateHTMLRenderer, renderers.JSONRenderer]

    def get(self, request, room_name: str, chat_type: str):
        data = {
            'room_name': room_name,
            'chat_type': chat_type
        }
        if chat_type == 'constant':
            if join_chat(request=request, room_name=room_name):
                return Response(data=data, status=status.HTTP_200_OK, template_name='chat/room.html')
            # TODO bad request template
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST, template_name='chat/room.html')
        return Response(data=data, status=status.HTTP_200_OK, template_name='chat/room.html')

    def post(self, request, room_name: str, chat_type: str):
        data = {
            'room_name': room_name,
            'chat_type': chat_type
        }
        if chat_type == 'constant':
            serializer_data = create_room(request=request, room_name=room_name)
            print(serializer_data)
            if not serializer_data:
                return Response(data=data, status=status.HTTP_200_OK, template_name='chat/room.html')
            # TODO set some template and delete exist, data => serializer_data
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST, template_name='chat/room.html')
        return Response(data=data, status=status.HTTP_200_OK, template_name='chat/room.html')


def index(request):
    return render(request=request, template_name='index.html')


def room(request, room_name: str, chat_type: str):
    if chat_type == 'constant':
        pass

    return render(request=request, template_name='chat/room.html', context={
        'room_name': room_name,
        'chat_type': chat_type
    })
