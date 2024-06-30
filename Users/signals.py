from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from .models import CustomUser, user_profile , Follow

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile.objects.create(user=instance)


@receiver(post_save, sender=user_profile)
def update_user_is_private(sender, instance, created, **kwargs):
    user = instance.user
    user.is_private = instance.is_private
    user.save()
    
    
@receiver(post_save,sender=Follow)
def update_followers_count(sender, instance, created, **kwargs):
    if created:
        instance.followed.user_profile.followers_count = Follow.objects.filter(followed=instance.followed).count()
        instance.followed.user_profile.save()
        instance.follower.user_profile.followings_count = Follow.objects.filter(follower=instance.follower).count()
        instance.follower.user_profile.save()

@receiver(post_delete, sender=Follow)
def update_followers_count_on_delete(sender, instance, **kwargs):
    instance.followed.user_profile.followers_count = Follow.objects.filter(followed=instance.followed).count()
    instance.followed.user_profile.save()
    instance.follower.user_profile.followings_count = Follow.objects.filter(follower=instance.follower).count()
    instance.follower.user_profile.save()
        