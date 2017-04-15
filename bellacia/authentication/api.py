# -*- coding: utf-8 -*-
from uuid import uuid4
from django.core.cache import cache
from rest_framework.decorators import api_view, authentication_classes
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from bellacia.core.authentications import BearerAuthentication


@api_view(['GET', 'POST', 'DELETE'])
@authentication_classes([BasicAuthentication, BearerAuthentication])
def authentication_view(request):
    if request.method == 'GET':
        token = request.auth
        data = {
            'token': token,
            'expires_in': cache.ttl(token),
            '_links': {
                'user': request.user.get_absolute_url()
            }
        }

        return Response(data, status=status.HTTP_200_OK, content_type='application/json')

    elif request.method == 'POST':
        token = uuid4().hex
        cache.set(token, request.user, timeout=3600)
        data = {
            'token': token,
            'expires_in': cache.ttl(token),
            '_links': {
                'user': request.user.get_absolute_url()
            }
        }

        return Response(data, status=status.HTTP_201_CREATED, content_type='application/json')

    elif request.method == 'DELETE':
        cache.delete(request.auth)

        return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')

    raise NotFound
