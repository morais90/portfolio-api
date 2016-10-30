# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import User
from .serializers import UserSerializer
from .filters import UserFilter


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilter
    ordering_fields = ('id', 'first_name', 'last_name', 'email')

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = (AllowAny,)
            return super().get_permissions()
