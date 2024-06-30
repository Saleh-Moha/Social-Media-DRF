from rest_framework import generics
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,AllowAny
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from .permissions import IsOwnerOrReadOnly,IsOnlyOwenr
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import ValidationError

class User_Profile_Info(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
        



class User_Profile(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_profile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        # Only allow access to the owner's profile or profiles they follow
        user = self.request.user
        if user.is_authenticated:
            return user_profile.objects.filter(
                Q(user=user) | 
                Q(user__followers__follower=user)
            )
        return user_profile.objects.filter(is_private=False)    






class Do_Follow(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        follower = self.request.user
        followed_id = self.kwargs['id']


        try:
            followed = CustomUser.objects.get(id=followed_id)
        except CustomUser.DoesNotExist:
            raise ValidationError("No user matches this id")

        if followed.is_private:
            # Create a follow request
            if Follow_Request.objects.filter(requester=follower, requested=followed, status='pending').exists():
                raise ValidationError("Follow request already sent")
            Follow_Request.objects.create(requester=follower, requested=followed)
            return Response("Follow request sent", status=status.HTTP_201_CREATED)
        else:
            # Directly create a follow relationship
            if Follow.objects.filter(follower=follower, followed=followed).exists():
                raise ValidationError("Already following this user")
            serializer.save(follower=follower, followed=followed)
        
            

class FollowRequest(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow_Request.objects.all()
    serializer_class = FollowRequestSerializer
    permission_classes = [IsOnlyOwenr]

    def perform_update(self, serializer):
        instance = self.get_object()
        # When a request is accepted, create a follow relationship and delete the follow request
        if serializer.validated_data.get('status') == 'accepted':
            Follow.objects.create(follower=instance.requester, followed=instance.requested)
            instance.delete()
        else:
            serializer.save()


class Followers(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = Followersserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(followed=user)
    

        
    
class Following(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = Followingserializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)