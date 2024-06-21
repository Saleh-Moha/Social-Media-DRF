from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser, user_profile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile.objects.create(user=instance)


@receiver(post_save, sender=user_profile)
def update_user_is_private(sender, instance, created, **kwargs):
    user = instance.user
    user.is_private = instance.is_private
    user.save()