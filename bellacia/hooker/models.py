from django.db import models


class Service(models.Model):
    name = models.CharField()


class Hooker(models.Model):
    name = modes.CharField(max_length=50)
    age = models.IntegerField()
    height = models.FloatField(decimal_places=2)
    weight = models.FloatField(decimal_places=2)
    services = models.ManyToMany(Service)


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
