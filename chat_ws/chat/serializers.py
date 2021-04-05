from rest_framework import serializers

from chat.models import Room, InvitedPerson


class RoomModelSerializer(serializers.ModelSerializer):
    """ Model serializer for room """

    class Meta:
        model = Room
        fields = '__all__'


class InvitedPersonModelSerializer(serializers.ModelSerializer):
    """ Model serializer for invited persons """

    name = serializers.CharField(read_only=True)

    class Meta:
        model = InvitedPerson
        fields = '__all__'
