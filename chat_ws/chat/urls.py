from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views
from .views import InvitedPersonModelViewSet

router = SimpleRouter()
router.register(r'invite_person', InvitedPersonModelViewSet)

urlpatterns = [
    path('chat/<str:room_name>/<str:chat_type>/', views.RoomAPIView.as_view(), name='room'),
] + router.urls
