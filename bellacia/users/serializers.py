from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_active')
        extra_args = {
            'id': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            }
        }
