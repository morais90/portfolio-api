# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import status

from .models import User, Group, Permission
from .serializers import UserSerializer, GroupSerializer, PermissionSerializer
from .filters import UserFilter, GroupFilter, PermissionFilter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    ordering_fields = ('id', 'first_name', 'last_name', 'email')

    def get_permissions(self):
        if self.action in ('create',):
            return (AllowAny(), )
        return super().get_permissions()

    @detail_route(methods=['GET'])
    def groups(self):
        user = self.get_objects()

        self.filter_class = GroupFilter
        queryset = self.filter_queryset(user.groups.all())
        page = self.paginate_queryset(queryset)
        serializer = GroupSerializer(page, many=True)

        if page is not None:
            return self.paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    ordering_fields = ('id', 'name')

    @detail_route(methods=['GET'])
    def permissions(self):
        group = self.get_objects()

        self.filter_class = PermissionFilter
        queryset = self.filter_queryset(group.permissions.all())
        page = self.paginate_queryset(queryset)
        serializer = PermissionSerializer(page, many=True)

        if page is not None:
            return self.paginated_response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')


class PermissionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    filter_class = PermissionFilter
    ordering_fields = ('id', 'name', 'codename')
