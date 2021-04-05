from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from auth_user.serializers import CustomTokenObtainPairSerializer


class LogInView(APIView):
    """View for login and take token"""

    def post(self, request):
        serializer = LogInSerializer(data=request.data)
        print(1)
        if serializer.is_valid():
            data = log_in(request=request, data=serializer.data)
            return Response(data=data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


