from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
from Users.models import user_profile
from Likes.models import Like_WrittenPosts,Like_SharedPosts
from Comments.models import Comment_WrittenPosts,Comment_SharedPosts
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


@receiver(post_save, sender=Like_WrittenPosts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.likes = Like_WrittenPosts.objects.filter(post=post).count()
        post.save()
        
@receiver(post_delete, sender=Like_WrittenPosts)
def update_likes_count_on_delete(sender, instance, **kwargs):
    post = instance.post
    post.likes = Like_WrittenPosts.objects.filter(post=post).count()
    post.save()
    

@receiver(post_save, sender=Comment_WrittenPosts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.comments = Comment_WrittenPosts.objects.filter(post=post).count()
        post.save()

@receiver(post_delete, sender=Comment_WrittenPosts)
def update_likes_count_on_delete(sender, instance, **kwargs):
        post = instance.post
        post.comments = Comment_WrittenPosts.objects.filter(post=post).count()
        post.save()


@receiver(post_save, sender=Shared_Posts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.shared_from
        post.shares = Shared_Posts.objects.filter(shared_from=post).count()
        post.save()
        
 
        


@receiver(post_save, sender=Like_SharedPosts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.likes = Like_SharedPosts.objects.filter(post=post).count()
        post.save()
        
@receiver(post_delete, sender=Like_SharedPosts)
def update_likes_count_on_delete(sender, instance, **kwargs):
        post = instance.post
        post.likes = Like_SharedPosts.objects.filter(post=post).count()
        post.save()

@receiver(post_save, sender=Comment_SharedPosts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.post
        post.comments = Comment_SharedPosts.objects.filter(post=post).count()
        post.save()

@receiver(post_delete, sender=Comment_SharedPosts)
def update_likes_count_on_delete(sender, instance, **kwargs):
        post = instance.post
        post.comments = Comment_SharedPosts.objects.filter(post=post).count()
        post.save()


@receiver(post_save, sender=Shared_Posts)
def update_likes_count_on_save(sender, instance, created, **kwargs):
    if created:
        post = instance.shared_from
        post.shares = Shared_Posts.objects.filter(shared_from=post).count()
        post.save()
        
        
