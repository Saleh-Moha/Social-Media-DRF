from django.db import models
from Users.models import CustomUser
from Posts.models import Written_Posts,Shared_Posts


class Like_WrittenPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    

class Like_SharedPosts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Shared_Posts,on_delete=models.CASCADE)