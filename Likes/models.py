from django.db import models
from Users.models import CustomUser
from Posts.models import Written_Posts,Shared_Posts


class Like_WrittenPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    

class Like_SharedPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Shared_Posts,on_delete=models.CASCADE)
    


class Like_Notification_on_WrittenPosts(models.Model):
    liker = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='wholikes')
    liked = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whohasbeenlikes')
    post = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    

class Like_Notification_on_SharedPosts(models.Model):
    liker = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='wholikesshared')
    liked = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='whohasbeenlikeshared')
    post = models.ForeignKey(Shared_Posts,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)