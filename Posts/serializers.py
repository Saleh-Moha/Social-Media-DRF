from rest_framework import serializers
from . models import *
from Users.serializers import CustomUserSerializer


class WrittenPostsSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Written_Posts
        fields = ['id','user','content','image','video','created_at']

class SharedPostsSerializer(serializers.ModelSerializer):
    shared_from = WrittenPostsSerializer(read_only=True)
    user = CustomUserSerializer(read_only=True)
    class Meta:
        model = Shared_Posts
        fields = ['id','user','content','created_at','shared_from']
