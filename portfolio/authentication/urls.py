# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import authentication_view


urlpatterns = [
    url(r'^$', authentication_view, name='api-auth'),
]
