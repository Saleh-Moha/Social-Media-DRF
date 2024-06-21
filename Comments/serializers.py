from rest_framework import serializers
from .models import *
from Users.serializers import CustomUserSerializer,UserSerializer
from Users.models import CustomUser as User
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
        
class LikeCountWrittenpostsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    data = CommentWrittenPostsSerializers(many=True)
    
class LikeCountSharedpostsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    data = CommentSharedPostsSerializers(many=True)