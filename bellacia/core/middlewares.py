# -*- coding: utf-8 -*-
from django import http


class CorsMiddleware:
    def process_request(self, request):
        if request.method == 'OPTIONS':
            return http.HttpResponse()
        return None

    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = 'Origin, Content-Type, Accept, Authorization'
        response['Access-Control-Allow-Methods'] = 'POST, GET, PUT, DELETE, OPTIONS'
        return response
