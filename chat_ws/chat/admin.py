from django.contrib import admin

from .models import Room, Message, InvitedPerson


@admin.register(Room)
class RoomModelAdmin(admin.ModelAdmin):
    """ Model admin for model room """

    pass


@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    """ Model admin for model message """

    pass


@admin.register(InvitedPerson)
class InvitedPersonModelAdmin(admin.ModelAdmin):
    """ Model admin for invited persons """

    pass
