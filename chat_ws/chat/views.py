from rest_framework import status, mixins, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from chat.models import InvitedPerson, Room
from chat.services_views import (
    create_room,
    join_chat,
    count_invited_persons,
    validate_invite_person,
)
from chat.serializers import InvitedPersonModelSerializer, RoomModelSerializer
from chat.tasks import send_invited_email
from chat.permissions import IsPostOrReadOnly


class RoomsViewSet(mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    """ View set for user rooms """

    queryset = Room.objects.all()
    serializer_class = RoomModelSerializer
    permission_classes = {permissions.IsAuthenticated}

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class InvitedPersonModelViewSet(mixins.CreateModelMixin,
                                mixins.DestroyModelMixin,
                                GenericViewSet):
    """ View set for Invited persons """

    queryset = InvitedPerson.objects.all()
    serializer_class = InvitedPersonModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        if validate_invite_person(request=request):
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                if count_invited_persons(request=request):
                    send_invited_email(
                        web_url='http://localhost:8080',
                        room_id=request.data['room'],
                        user_id=request.data['user'])
                    return super().create(request, *args, **kwargs)
                else:
                    return Response(data={'error': 'You can invite only 3 users'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'error': 'user does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class RoomAPIView(APIView):
    """ API view for room """

    permission_classes = [IsPostOrReadOnly]

    def get(self, request, room_name: str, chat_type: str):
        data = {
            'room_name': room_name,
            'chat_type': chat_type
        }
        if chat_type == 'constant':
            if join_chat(request=request, room_name=room_name):
                return Response(data=data, status=status.HTTP_200_OK)
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data, status=status.HTTP_200_OK)

    def post(self, request, room_name: str, chat_type: str):
        if chat_type == 'constant':
            serializer_data = create_room(request=request, room_name=room_name)
            if len(serializer_data) > 1:
                return Response(data=serializer_data, status=status.HTTP_201_CREATED)
            return Response(data=serializer_data, status=status.HTTP_400_BAD_REQUEST)
