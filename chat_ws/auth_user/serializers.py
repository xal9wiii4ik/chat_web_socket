from rest_framework import serializers


class LogInSerializer(serializers.Serializer):
    """Serializer for log in"""

    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(max_length=128, required=True)
