# -*- coding:utf-8 -*-
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.exceptions import NotFound

from .models import Model, Character, Contact
from .serializers import ModelSerializer, CharacterSerializer, ContactSerializer


class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

    @detail_route(methods=['POST', 'GET'])
    def communications(self, request, pk=None):
        model = self.get_object()

        if request.method == 'POST':
            data = request.data
            data.update({
                'model': model.id
            })
            serializer = ContactSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')

        elif request.method == 'GET':
            queryset = model.contact_set.all()
            page = self.paginate_queryset(queryset)
            serializer = ContactSerializer(queryset, many=True)

            if page is not None:
                return self.paginated_response(serializer.data)

            return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')

    @detail_route(methods=['POST', 'DELETE'], parser_classes=[MultiPartParser])
    def picture(self, request, pk=None):
        model = self.get_object()

        if request.method == 'POST' and not model.picture:
            serializer = ModelSerializer(model, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')

        elif request.method == 'DELETE' and model.picture:
            model.picture.delete()

            return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')

        raise NotFound


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
