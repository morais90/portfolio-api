from django.db import models


class Customer(models.Model)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey('authentication.User')
