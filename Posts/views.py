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
from .permissions import IsOwnerOrReadOnly,IsOwnerPrivate
from rest_framework.exceptions import NotAuthenticated
from Users.models import Follow
from rest_framework.exceptions import PermissionDenied
class WritePosts(generics.CreateAPIView):
    queryset = Written_Posts.objects.all()
    serializer_class = WrittenPostsSerializer
    permission_classes = [IsAuthenticated]
    

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)
        
class SharePosts(generics.CreateAPIView):
    queryset = Shared_Posts
    serializer_class = SharedPostsSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['id']
        post_username= self.kwargs['username']
        try:
            post = Written_Posts.objects.get(user__username=post_username,id=post_id)
        except Written_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer.save(user=user, shared_from=post)
        



class EditWrittenPosts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Written_Posts.objects.all()
    serializer_class = WrittenPostsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
            

class EditSharedPosts(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shared_Posts.objects.all()
    serializer_class = SharedPostsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
    
class Written_posts_list(generics.ListAPIView):
    queryset = Written_Posts.objects.all()
    serializer_class = WrittenPostsSerializer
    permission_classes = [IsOwnerPrivate]

    def get_queryset(self):
        user = self.request.user
        post_owner_id = self.kwargs['id']  # ID of the post owner
        queryset = Written_Posts.objects.filter(user_id=post_owner_id)

        if not user.is_authenticated:
            # If the user is not authenticated, only return non-private posts
            queryset = queryset.filter(is_private=False)
            if not queryset.exists():
                raise PermissionDenied("This account is private")
            return queryset


        if user.id != post_owner_id:
            # Filter out private posts if the user is not the owner and not a follower
            queryset = queryset.filter(
                Q(user=user) | 
                Q(is_private=False) | 
                Q(user__followers__follower=user)
            )
        if not queryset.exists():
            raise PermissionDenied("This account is private")
        
        return queryset



class Shared_posts_list(generics.ListAPIView):
    queryset = Shared_Posts.objects.all()
    serializer_class = SharedPostsSerializer
    permission_classes = [IsOwnerPrivate]

    def get_queryset(self):
        user = self.request.user
        id = self.kwargs['id']
        queryset =Shared_Posts.objects.filter(user_id=id)

        # If the requesting user is not the owner, filter out private posts
        if user.id != id:
            queryset = queryset.filter(is_private=False)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response('no posts for this user', status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)