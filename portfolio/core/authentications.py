# -*- coding: utf-8 -*-
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.core.cache import cache


class BearerAuthentication(BaseAuthentication):
    www_authenticate_realm = 'api'

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != b'bearer':
            return None

        if len(auth) == 1 or len(auth) > 2:
            raise exceptions.AuthenticationFailed('invalid_header')
        elif len(auth) > 2:
            raise exceptions.AuthenticationFailed('invalid_header')

        return self.authenticate_credentials(auth[1])

    def authenticate_credentials(self, key):
        user = cache.get(key.decode())

        if not user:
            return None

        if not user.is_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, key)

    def authenticate_header(self, request):
        return 'Bearer realm="{}"'.format(self.www_authenticate_realm)
