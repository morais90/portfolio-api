from rest_framework import serializers
from .models import User, Group, Permission


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
            'password': {
                'write_only': True
            },
            'groups': {
                'write_only': True,
                'many': True,
                'allow_null': True
            }
        }


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'permissions': {
                'write_only': True,
                'many': True,
                'allow_null': True
            }
        }


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'name', 'codename')
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'name': {
                'read_only': True
            },
            'codename': {
                'read_only': True
            }
        }
