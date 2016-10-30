from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'full_name', 'email', 'password', 'is_active')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'is_active': {
                'read_only': True
            },
            'first_name': {
                'write_only': True
            },
            'last_name': {
                'write_only': True
            },
            'password': {
                'write_only': True
            }
        }
