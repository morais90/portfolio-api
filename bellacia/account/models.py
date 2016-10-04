# -*- coding: utf-8 -*_
from django.db import models


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    interval = models.DurationField()
    cost = models.DecimalField(decimal_places=2)


class Subscribe(models.Model):
    customer = models.ForeignKey('customer.Customer')
    payment_date = models.DatetimeField()
    expiration_date = models.DatetimeField()
    Subscription = models.ForeignKey(Subscription)


class SectionSubscribe(models.Model):
    customer = models.ForeignKey('customer.Customer')
    section = models.ForeignKey('essay.Section')
    payment_date = models.DatetimeField()
    expiration_date = models.DatetimeField()
