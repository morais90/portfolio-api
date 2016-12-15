# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'^auth/', include('bellacia.authentications.urls')),
    url(r'^users/', include('bellacia.users.urls')),
    url(r'^hookers/', include('bellacia.hooker.urls'))
]
