# -*- coding: utf-8 -*_
from django.db import models


class Subscription(models.Model):
    name = models.CharField('Nome da assinatura', max_length=50)
    interval = models.DurationField('Validade')
    cost = models.DecimalField('Custo', decimal_places=2)


class Subscribe(models.Model):
    user = models.ForeignKey('user.User')
    payment_date = models.DatetimeField('Data de pagamento')
    expiration_date = models.DatetimeField('Data de finalização')
    Subscription = models.ForeignKey(Subscription)


class SectionSubscribe(models.Model):
    customer = models.ForeignKey('user.User')
    section = models.ForeignKey('essay.Section')
    payment_date = models.DatetimeField('Data de pagamento')
    expiration_date = models.DatetimeField('Data de finalização')
