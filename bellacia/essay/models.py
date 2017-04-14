# -*- coding: utf-8 -*-
from django.db import models


class Section(models.Model):
    model = models.ForeignKey('model.Model')
    cost = models.DecimalField(max_digits=5, decimal_places=2, default=0.99)


class Photo(models.Model):
    section = models.ForeignKey(Section)
    image = models.ImageField(upload_to='section-photos')
    public = models.BooleanField(default=False)
    description = models.TextField()


class Video(models.Model):
    section = models.ForeignKey(Section)
    video = models.FileField(upload_to='section-videos')
    public = models.BooleanField(default=False)
    description = models.TextField()
