from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView

from auth_user.views import CustomTokenObtainPairView

urlpatterns = [
    path('', include('chat.urls')),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='login'),
]
