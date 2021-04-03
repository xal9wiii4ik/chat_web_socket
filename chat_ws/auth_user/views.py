from django.db import IntegrityError

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_user.serializers import (
    LogInSerializer,
)
from auth_user.services_view import (
    log_in,
)


class LogInView(APIView):
    """View for login and take token"""

    def post(self, request):
        serializer = LogInSerializer(data=request.data)
        if serializer.is_valid():
            data = log_in(request=request, data=serializer.data)
            return Response(data=data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
