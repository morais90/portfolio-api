# -*- coding: utf-8 -*-
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=50)


def model_picture_directory(instance, filename):
    return 'model/{}/pictures/{}'.format(instance.id, filename)


class Model(models.Model):
    name = models.CharField('Nome', max_length=50)
    picture = models.ImageField('Foto', upload_to=model_picture_directory, null=True)
    age = models.IntegerField('Idade')
    height = models.FloatField('Altura')
    weight = models.FloatField('Peso')
    character = models.ManyToManyField(Character)
    is_active = models.BooleanField('Ativo', default=True)

    def delete(self):
        self.is_active = False
        self.save()


class Contact(models.Model):
    EMAIL = 'email'
    PHONE = 'phone'
    WHATSAPP = 'whatsapp'

    CONTACT_CHOICES = (
        ('email', 'E-mail'),
        ('phone', 'Phone'),
        ('whatsapp', 'WhatsApp')
    )

    type = models.CharField('Tipo de contato', max_length=6, choices=CONTACT_CHOICES)
    contact = models.CharField('Contato', max_length=254)
    model = models.ForeignKey(Model)
