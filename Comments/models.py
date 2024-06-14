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