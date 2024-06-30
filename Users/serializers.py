from djoser.serializers import UserCreateSerializer, UserSerializer # type: ignore
from rest_framework import serializers
from .models import CustomUser,user_profile,Follow,Follow_Request

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','username', 'first_name', 'last_name', 'date_of_birth', 'password')
        def validate(self, data):
            if not data.get('email'):
                raise serializers.ValidationError({'email': 'This field is required.'})
            if not data.get('first_name'):
                raise serializers.ValidationError({'first_name': 'This field is required.'})
            if not data.get('last_name'):
                raise serializers.ValidationError({'last_name': 'This field is required.'})
            if not data.get('date_of_birth'):
                raise serializers.ValidationError({'date_of_birth': 'This field is required.'})
            return data
    
class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','username' ,'first_name', 'last_name', 'date_of_birth')

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']
    
class UserProfileSerializer(serializers.ModelSerializer):
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = user_profile
        fields = '__all__'
      

class FollowSerializer(serializers.ModelSerializer):
    follower = UsernameSerializer(read_only=True)
    followed = UsernameSerializer(read_only=True)
    class Meta:
        model = Follow
        fields = ['id','follower','followed','created_at']
        
class FollowRequestSerializer(serializers.ModelSerializer):
    # requester = UsernameSerializer(read_only=True)
    # requested = UsernameSerializer(read_only=True)
    message = serializers.SerializerMethodField()

    class Meta:
        model = Follow_Request
        fields = ['message','id', 'status', 'created_at']
    
    def get_message(self, obj):
        return f"{obj.requester.username} has sent you a follow request"
        

class Followersserializer(serializers.ModelSerializer):
    follower = UsernameSerializer(read_only=True)
    class Meta:
        model = Follow
        fields = ['follower']


    
        

class Followingserializer(serializers.ModelSerializer):
    followed = UsernameSerializer(read_only=True)
    class Meta:
        model = Follow
        fields = ['followed']