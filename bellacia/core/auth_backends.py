# -*- coding: utf-8 -*-
from bellacia.user.models import User


class UserBackend:
    def authenticate(self, email=None, password=None):
        user = self.get_user(email)

        if not user.is_active:
            return None
        elif not user.check_password(password):
            return None

        return user

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
