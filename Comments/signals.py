from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from .models import *


@receiver(post_save,sender = Comment_WrittenPosts)
def create_notification(sender,instance,created,**kwargs):
    if created:
        post = instance.post
        Comment_Notification_on_WrittenPosts.objects.create(post=post,commenter=instance.user,commented=post.user)
        

@receiver(post_save,sender = Comment_SharedPosts)
def create_notification(sender,instance,created,**kwargs):
    if created:
        post = instance.post
        Comment_Notification_on_SharedPosts.objects.create(post=post,commenter=instance.user,commented=post.user)