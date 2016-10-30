# -*- coding: utf-8 -*-
from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls
