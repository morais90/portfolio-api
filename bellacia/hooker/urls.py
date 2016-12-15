# -*- coding: utf-8 -*-
from rest_framework import routers
from .api import HookerViewSet, ServiceViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'', HookerViewSet)

urlpatterns = router.urls
