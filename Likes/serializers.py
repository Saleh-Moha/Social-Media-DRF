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
        
class LikeCountWrittenpostsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    data = LikeWrittenPostsSerializers(many=True)
    
class LikeCountSharedpostsSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    data = LikeSharedPostsSerializers(many=True)