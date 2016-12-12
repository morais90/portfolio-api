# -*- coding: utf-8 -*-
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=50)


def hooker_picture_directory(instance, filename):
    return 'hooker/{}/pictures/{}'.format(instance.id, filename)


class Hooker(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=hooker_picture_directory)
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
    hooker = models.ForeignKey(Hooker)
