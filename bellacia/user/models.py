# -*- coding: utf-8 -*-
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission

from .managers import UserManager


__all__ = ['User', 'Group', 'Permission']


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Ativo', default=True)
    receive_email = models.BooleanField('Recebe e-mails', default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.id})

    def delete(self):
        self.is_active = False
        self.save()
