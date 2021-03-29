from rest_framework.serializers import ModelSerializer

from chat.models import Room, InvitedPerson


class RoomModelSerializer(ModelSerializer):
    """ Model serializer for room """

    class Meta:
        model = Room
        fields = '__all__'


class InvitedPersonModelSerializer(ModelSerializer):
    """ Model serializer for invited persons """

    class Meta:
        model = InvitedPerson
        fields = '__all__'
