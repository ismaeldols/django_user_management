from django.dispatch import receiver
from django.db.models.signals import post_save
from admin_sso.models import Assignment

from .models import CustomUser


@receiver(signal=post_save, dispatch_uid='post_save_user_uid', sender=CustomUser)
def add_admin_assigments(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        assigment = Assignment.objects.create(username_mode=1, username=instance.email.split('@', 1)[0],
                                              domain=instance.email.split('@', 1)[1],
                                              copy=False, weight=100, user=instance)
        assigment.save()


