from django.db import models
from Users.models import CustomUser
from Posts.models import Written_Posts,Shared_Posts


class Comment_WrittenPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    

class Comment_SharedPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Shared_Posts,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    
    
class Comment_Notification_on_WrittenPosts(models.Model):
    commenter = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whocomments')
    commented = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whohasbeencommented')
    post = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    

class Comment_Notification_on_SharedPosts(models.Model):
    commenter = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whocommentsshared')
    commented = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whohasbeencommentedhared')
    post = models.ForeignKey(Shared_Posts,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)