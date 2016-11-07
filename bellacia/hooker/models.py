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
    EMAIL = 'email'
    PHONE = 'phone'
    WHATSAPP = 'whatsapp'

    CONTACT_CHOICES = (
        ('email', 'E-mail'),
        ('phone', 'Phone'),
        ('whatsapp', 'WhatsApp')
    )

    kind = models.CharField(max_length=6, choices=CONTACT_CHOICES)
    contact = models.CharField(max_length=254)
