# -*- coding: utf-8 -*-
from django import http


def cors_middleware(get_response):
    def middleware(request):
        if request.method == 'OPTIONS':
            return http.HttpResponse()

        response = get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization'
        response['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
        return response
    return middleware
