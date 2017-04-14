# -*- coding: utf-8 -*-
from rest_framework import routers
from .api import UserViewSet, GroupViewSet, PermissionViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = router.urls
