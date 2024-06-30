from rest_framework import serializers
from .models import *
from Users.serializers import CustomUserSerializer,UserSerializer
from Users.models import CustomUser as User
from Posts.serializers import *


class LikeWrittenPostsSerializers(serializers.ModelSerializer):
    post = WrittenPostsSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Like_WrittenPosts
        fields = ['id','post','user']
        

class LikeSharedPostsSerializers(serializers.ModelSerializer):
    post =  SharedPostsSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Like_SharedPosts
        fields = ['id','post','user']
        
class WrittenPostsLikeNotificationSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Like_Notification_on_WrittenPosts 
        fields = ['message','id','created_at']
        
    def get_message(self,obj):
            return f'{obj.liker} liked your post {obj.post}'
        
class SharedPostsLikeNotificationSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Like_Notification_on_SharedPosts 
        fields = ['message','id','created_at']
        
    def get_message(self,obj):
            return f'{obj.liker} liked your post {obj.post}'