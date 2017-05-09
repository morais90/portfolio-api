# -*- coding: utf-8 -*-
from rest_framework import routers
from .api import ModelViewSet, CharacterViewSet, ContactViewSet

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'', ModelViewSet)

urlpatterns = router.urls
