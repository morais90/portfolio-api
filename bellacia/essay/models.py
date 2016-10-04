from django.db import models


class Section(models.Model):
    hooker = models.ForeignKey('hooker.Hooker')
    public = models.BooleanField(default=False)
    cost = models.DecimalField(default=0.99)


class Photo(models.Model):
    section = models.ForeignKey(Section)
    image = models.ImageField(upload_to='section-photos')
    description = models.TextField()


class Video(models.Model):
    section = models.ForeignKey(Section)
    video = models.FileField(upload_to='section-videos')
    description = models.TextField()
