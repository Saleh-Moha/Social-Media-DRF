from djoser.serializers import UserCreateSerializer, UserSerializer # type: ignore
from rest_framework import serializers
from .models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','username','location','bio','phone_number', 'first_name', 'last_name', 'date_of_birth', 'password')
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
        fields = ('id', 'email','username','location','bio','phone_number', 'first_name', 'last_name', 'date_of_birth', 'profile_photo')
