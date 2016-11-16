# -*- coding: utf-8 -*-
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

from .managers import UserManager


__all__ = ['User', 'Group', 'Permission']


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = UserManager()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name).strip()

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})

    def delete(self):
        self.is_active = False
        self.save()
