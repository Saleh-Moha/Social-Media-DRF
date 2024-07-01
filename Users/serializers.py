from djoser.serializers import UserCreateSerializer, UserSerializer # type: ignore
from rest_framework import serializers
from .models import CustomUser,user_profile,Follow,Follow_Request

# the serializer used to register users 
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

# serilizer for user info
class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','username' ,'first_name', 'last_name', 'date_of_birth')

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username']
    
# profile serializer
class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = user_profile
        fields = '__all__'
      
# follow process serializer
class FollowSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Follow
        fields = ['id','message','created_at']
        
    def get_message(self,obj):
        return f'you now follow {obj.followed.username}'

# follow requests 
class FollowRequestsSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Follow_Request
        fields = ['message','id','created_at']
    
    def get_message(self, obj):
        return f"{obj.requester.username} has sent you a follow request"


# follow request handeling serializer
class FollowRequestHandelingSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Follow_Request
        fields = ['message','id', 'status', 'created_at']
    
    def get_message(self, obj):
        return f"{obj.requester.username} has sent you a follow request"
        
# follower serializer
class FollowersSerializer(serializers.ModelSerializer):
    follower = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Follow
        fields = ['follower']

# following serializer 
class FollowingSerializer(serializers.ModelSerializer):
    followed = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Follow
        fields = ['followed']