from rest_framework.request import Request

from chat.serializers import RoomModelSerializer
from chat.models import Room, InvitedPerson


def create_room(request: Request, room_name: str) -> bool or dict:
    """ Function for creating the room """

    rooms = Room.objects.filter(owner_id=request.user.id)
    if len(rooms) >= 3:
        return {'error': 'You just have 3 or more rooms'}
    for room in rooms:
        if room.name == room_name:
            return {'error': 'Room with this room_name already exist'}
    serializer = RoomModelSerializer(data={'owner': request.user.id, 'name': room_name})
    if serializer.is_valid():
        RoomModelSerializer.create(serializer, serializer.validated_data)
        return False
    else:
        return serializer.errors


def join_chat(request: Request, room_name: str) -> bool:
    """ Verification if user in list of invited persons """

    try:
        InvitedPerson.objects.get(user=request.user, room__name=room_name)
        return True
    except Exception:
        return False


def count_invited_persons(request: Request) -> bool:
    """ Checking exist invited persons in the room """

    room = Room.objects.get(id=request.data['room'])
    print(room)
    if room.owner != request.user:
        print(1)
        return False
    persons = InvitedPerson.objects.filter(room__id=request.data['room'])
    print(persons)
    if len(persons) >= 3:
        return False
    return True
