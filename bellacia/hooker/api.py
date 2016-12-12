# -*- coding:utf-8 -*-
from rest_framework import viewsets

from .models import Hooker, Service, Contact
from .serializers import HookerSerializer, ServiceSerializer, ContactSerializer


class HookerViewSet(viewsets.ModelViewSet):
    queryset = Hooker.objects.all()
    serializer_class = HookerSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ConctactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
