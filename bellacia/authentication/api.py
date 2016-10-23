# -*- coding: utf-8 -*-
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
