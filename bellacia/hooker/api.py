# -*- coding:utf-8 -*-
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import Hooker, Service, Contact
from .serializers import HookerSerializer, ServiceSerializer, ContactSerializer


class HookerViewSet(viewsets.ModelViewSet):
    queryset = Hooker.objects.all()
    serializer_class = HookerSerializer

    @detail_route(methods=['POST', 'GET'])
    def communications(self, request, pk=None):
        hooker = self.get_object()

        if request.method == 'POST':
            data = request.data
            data.update({
                'hooker': hooker.id
            })
            serializer = ContactSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')

        elif request.method == 'GET':
            queryset = hooker.contact_set.al()
            page = self.paginate_queryset(queryset)
            serializer = ContactSerializer(queryset, many=True)

            if page is not None:
                return self.paginated_response(serializer.data)

            return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
