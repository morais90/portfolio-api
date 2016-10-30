from django.db.models.signals import post_save
from django.dispatch import receiver
from guardian.shortcuts import assign_perm

from .models import User


@receiver(post_save, sender=User)
def user_post_save(sender, **kwargs):
    user = kwargs.get('instance')

    assign_perm('change_user', user, user)
    assign_perm('delete_user', user, user)
