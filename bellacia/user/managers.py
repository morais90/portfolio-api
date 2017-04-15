# -*- coding: utf-8 -*-
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password):
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.model(email=self.normalize_email(email), is_superuser=True)
        user.set_password(password)
        user.save(using=self._db)

        return user
