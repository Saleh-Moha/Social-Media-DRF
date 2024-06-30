from rest_framework import serializers
from .models import *
from Users.serializers import CustomUserSerializer
from Posts.serializers import *


class CommentWrittenPostsSerializers(serializers.ModelSerializer):
    post = WrittenPostsSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Comment_WrittenPosts
        fields = ['id','post','user','comment']
        

class CommentSharedPostsSerializers(serializers.ModelSerializer):
    post =  SharedPostsSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    
    class Meta:
        model = Comment_SharedPosts
        fields = ['id','post','user','comment']
        
class WrittenPostsCommentNotificationSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Comment_Notification_on_WrittenPosts
        fields = ['message','id','created_at']
    def get_message(self,obj):
        return f'{obj.commenter} commented on your post :  {obj.post}'
    

class SharedPostsCommentNotificationSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Comment_Notification_on_SharedPosts
        fields = ['message','id','created_at']
    def get_message(self,obj):
        return f'{obj.commenter} commented on your post {obj.post}'