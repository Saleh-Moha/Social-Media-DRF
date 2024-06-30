from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from .models import Like_WrittenPosts,Like_SharedPosts,Like_Notification_on_WrittenPosts, Like_Notification_on_SharedPosts


@receiver(post_save,sender=Like_WrittenPosts)
def create_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        Like_Notification_on_WrittenPosts.objects.create(post=post,liker=instance.user,liked=post.user)
        
@receiver(post_save,sender=Like_SharedPosts)
def create_notification(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        Like_Notification_on_SharedPosts.objects.create(post=post,liker=instance.user,liked=post.user)