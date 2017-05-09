# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework import exceptions


def error_handler(exc, context):
    data = {}

    if isinstance(exc, exceptions.NotAuthenticated):
        data['error'] = 'invalid_credential'

    return Response(data, status=exc.status_code)
