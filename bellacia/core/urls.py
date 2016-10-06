# -*- coding: utf-8 -*-
from django.conf.urls import url
from bellacia.dashboard import views


urlpatterns = [
    url(r'^dashboard/$', views.index),
]
