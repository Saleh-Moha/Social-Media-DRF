from rest_framework import generics
from django.db.models import Q
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly,IsOnlyOwenr
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

# user profile info that he signed up with
class User_Profile_Info(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsOwnerOrReadOnly]

# user profile info that will appear in thier profile
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

# follow proccess 
# 1- do follow function checks if the account is pricate or not
class Do_Follow(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # the follow process
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
            raise ValidationError(f"Follow request sent to {followed}")
        else:
            # Directly create a follow relationship
            if Follow.objects.filter(follower=follower, followed=followed).exists():
                raise ValidationError("Already following this user")
            serializer.save(follower=follower, followed=followed)

# 3- list the requests
class Follow_Requests(generics.ListAPIView):
    serializer_class = FollowRequestsSerializer
    
    def get_queryset(self):
        user = self.request.user 
        return Follow_Request.objects.filter(requested=user)
            
        
    def list(self, request, *args, **kwargs):
        user = self.request.user 
        if not user.is_authenticated:
            return Response({"detailed":"you don not have and account signup first"},status=status.HTTP_401_UNAUTHORIZED)
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response('there is no follow requests', status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)





# 3- handle the follow requests  
class Follow_Request_Handeling(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow_Request.objects.all()
    serializer_class = FollowRequestHandelingSerializer
    permission_classes = [IsOnlyOwenr]  
    # checks the status of the request  
    def perform_update(self, serializer):
        instance = self.get_object()
        # When a request is accepted, create a follow relationship and delete the follow request
        if serializer.validated_data.get('status') == 'accepted':
            Follow.objects.create(follower=instance.requester, followed=instance.requested)
            instance.delete()
        else:
            serializer.save()

# get the followers data 
class Followers(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowersSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(followed=user)

#  get the followings daata
class Following(generics.ListAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(follower=user)