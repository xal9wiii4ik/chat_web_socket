from rest_framework_simplejwt.views import TokenObtainPairView

from auth_user.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


