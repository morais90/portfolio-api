# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/auth/', include('bellacia.authentication.urls')),
    url(r'^v1/users/', include('bellacia.user.urls')),
    url(r'^v1/models/', include('bellacia.model.urls'))
]
