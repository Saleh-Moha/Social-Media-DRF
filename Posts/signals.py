from django.dispatch import receiver
from django.db.models.signals import post_save
from Users.models import user_profile
from Posts.models import Written_Posts , Shared_Posts # Import the Written_Posts model

@receiver(post_save, sender=user_profile)
def update_user_is_private(sender, instance, created, **kwargs):
    user = instance.user
    # Update all Written_Posts instances for this user
    Written_Posts.objects.filter(user=user).update(is_private=instance.is_private)


@receiver(post_save, sender=user_profile)
def update_user_is_private(sender, instance, created, **kwargs):
    user = instance.user
    # Update all Written_Posts instances for this user
    Shared_Posts.objects.filter(user=user).update(is_private=instance.is_private)
