# -*- coding: utf-8 -*-
from django.conf.urls import url, include


urlpatterns = [
    url(r'^v1/auth/', include('portfolio.authentication.urls')),
    url(r'^v1/users/', include('portfolio.user.urls')),
    url(r'^v1/models/', include('portfolio.model.urls'))
]
