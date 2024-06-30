from django.db import models
from django.conf import settings


# posts model setups


    
class Written_Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(max_length=1500,blank=False)
    image = models.ImageField(blank=True)
    video = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now=True)
    is_private = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{str(self.user)} writes this post {self.content}"
class Shared_Posts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField(max_length=1500,blank=True)
    created_at = models.DateTimeField(auto_now=True)    
    shared_from = models.ForeignKey(Written_Posts,on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
   
    
    def __str__(self):
        return f"{str(self.user)} shared this post from  {str(self.shared_from.user )}"