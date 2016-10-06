# -*- coding: utf-8 -*-
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)


class Hooker(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    services = models.ManyToManyField(Service)


class Contact(models.Model):
    EMAIL = 'EM'
    PHONE = 'PH'
    WHATSAPP = 'WH'

    CONTACT_CHOICES = (
        (EMAIL, 'E-mail'),
        (PHONE, 'Phone'),
        (WHATSAPP, 'WhatsApp')
    )

    kind = models.CharField(max_length=2, choices=CONTACT_CHOICES)
    number = models.CharField(max_length=11, null=True)
    email = models.EmailField(null=True)
