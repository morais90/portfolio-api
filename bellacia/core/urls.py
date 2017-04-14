# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'^auth/', include('bellacia.authentication.urls')),
    url(r'^users/', include('bellacia.user.urls')),
    url(r'^hookers/', include('bellacia.model.urls'))
]
