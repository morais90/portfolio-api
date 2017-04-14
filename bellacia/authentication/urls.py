# -*- coding: utf-8 -*-
from django.conf.urls import url
from .api import LoginView, LogoutView, RefreshView


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name='api-auth-login'),
    url(r'^logout/$', LogoutView.as_view(), name='api-auth-logout'),
    url(r'^refresh/$', RefreshView.as_view(), name='api-auth-refresh')
]
