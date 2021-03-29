from django.contrib.auth import get_user_model
from django.db import models


class Room(models.Model):
    """ Model room """

    name = models.CharField(max_length=30, verbose_name='Имя чата')
    owner = models.ForeignKey(to=get_user_model(),
                              related_name='room_owner',
                              on_delete=models.CASCADE)

    def __str__(self):
        return f'id: {self.pk}, name: {self.name}, owner: {self.owner.username}'

    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'


class Message(models.Model):
    """ Model message for room """

    text = models.TextField(verbose_name='Текст')
    room = models.ForeignKey(to=Room,
                             related_name='message_room',
                             on_delete=models.CASCADE)
    owner = models.ForeignKey(to=get_user_model(),
                              related_name='message_owner',
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)

    def __str__(self):
        return f'room: {self.room.name}, text: {self.text}, user: {self.owner.username}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class InvitedPerson(models.Model):
    """ Model for invited persons """

    user = models.ForeignKey(to=get_user_model(), related_name='invited_user', on_delete=models.CASCADE)
    room = models.ForeignKey(to=Room, related_name='invited_room', on_delete=models.CASCADE)

    def __str__(self):
        return f'room: {self.room.name}, user: {self.user.username}'

    class Meta:
        verbose_name = 'Приглашение'
        verbose_name_plural = 'Приглашенные'
