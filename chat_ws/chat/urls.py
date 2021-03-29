from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import SimpleRouter

from . import views
from .views import InvitedPersonModelViewSet

router = SimpleRouter()
router.register(r'invite_person', InvitedPersonModelViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/<str:chat_type>/', views.RoomAPIView.as_view(), name='room'),
    path('token/', TokenObtainPairView.as_view(), name='token')
] + router.urls
