# Generated by Django 3.1.7 on 2021-03-25 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0003_auto_20210321_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvitedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_room', to='chat.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Приглашение',
                'verbose_name_plural': 'Приглашенные',
            },
        ),
    ]
