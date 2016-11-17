# -*- coding: utf-8 -*-
from uuid import uuid4
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response


class LoginView(APIView):
    authentication_classes = (BasicAuthentication,)

    def post(self, request):
        token = uuid4().hex
        cache.set(token, request.user, timeout=3600)
        data = {
            'token': token,
            'expires_in': cache.ttl(token),
            '_links': {
                'user': request.user.get_absolute_url()
            }
        }

        return Response(data, status=status.HTTP_202_ACCEPTED, content_type='application/json')


class LogoutView(APIView):
    def post(self, request):
        cache.delete(request.auth)

        return Response(status=status.HTTP_202_ACCEPTED, content_type='application/json')


class RefreshView(APIView):
    def post(self, request):
        token = request.auth
        cache.expire(token, timeout=3600)
        data = {
            'token': token,
            'expires_in': cache.ttl(token)
        }

        return Response(data, status=status.HTTP_202_ACCEPTED, content_type='application/json')
