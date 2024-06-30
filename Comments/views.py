from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes,api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404
from Users.models import CustomUser
from Users.serializers import CustomUserSerializer
from Posts.models import *
from .permission import IsOwnerOrReadOnly
from datetime import timedelta
from django.utils import timezone

class Commentwrittenposts(generics.CreateAPIView):
    queryset = Comment_WrittenPosts.objects.all()
    serializer_class = CommentWrittenPostsSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['id']
        try:
            post = Written_Posts.objects.get(id=post_id)
        except Written_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Comment_WrittenPosts.objects.filter(user=user, post=post).exists():
            return Response({"detial":"you have already liked it"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(user=user, post=post)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
       
class Commentsharedposts(generics.CreateAPIView):
    queryset = Comment_SharedPosts.objects.all()
    serializer_class = CommentSharedPostsSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['id']
        try:
            post = Shared_Posts.objects.get(id=post_id)
        except Shared_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Comment_SharedPosts.objects.filter(user=user, post=post).exists():
            return Response({"detial":"you have already liked it"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(user=user, post=post)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

class Comment_writtenpost_list(generics.ListAPIView):
    queryset = Comment_WrittenPosts.objects.all()
    serializer_class = CommentWrittenPostsSerializers
    
    def get_queryset(self):
        post_id = self.kwargs['id']
        try:
            post =  Written_Posts.objects.get(id=post_id)
        except Written_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Comment_WrittenPosts.objects.filter(post=post)
    
    
class Comment_sharedpost_list(generics.ListAPIView):
    queryset = Comment_SharedPosts.objects.all()
    serializer_class = CommentSharedPostsSerializers
    
    def get_queryset(self):
        post_id = self.kwargs['id']
        try:
            post =  Shared_Posts.objects.get(id=post_id)
        except Shared_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Comment_SharedPosts.objects.filter(post=post)
    

class Comment_Delete_writtenpost(generics.DestroyAPIView):
    queryset = Comment_WrittenPosts.objects.all()
    serializer_class = CommentWrittenPostsSerializers
    permission_classes = [IsOwnerOrReadOnly]
    
class Comment_Delete_sharedposts(generics.DestroyAPIView):
    queryset = Comment_SharedPosts.objects.all()
    serializer_class = CommentSharedPostsSerializers
    permission_classes = [IsOwnerOrReadOnly]

class Written_Posts_Comments_Notification(generics.ListAPIView):
    serializer_class = WrittenPostsCommentNotificationSerializer
    def get_queryset(self):
        user = self.request.user
        # Calculate the cutoff time for 24 hours ago
        cutoff_time = timezone.now() - timedelta(hours=24)
        # Delete notifications older than 24 hours
        Comment_Notification_on_WrittenPosts.objects.filter(created_at__lt=cutoff_time).delete()
        # Return the queryset of notifications for the user
        return Comment_Notification_on_WrittenPosts.objects.filter(commented=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response('no comments', status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        
class Shared_Posts_Comments_Notification(generics.ListAPIView):
    serializer_class = SharedPostsCommentNotificationSerializer
    def get_queryset(self):
        user = self.request.user
        # Calculate the cutoff time for 24 hours ago
        cutoff_time = timezone.now() - timedelta(hours=24)
        # Delete notifications older than 24 hours
        Comment_Notification_on_SharedPosts.objects.filter(created_at__lt=cutoff_time).delete()
        # Return the queryset of notifications for the user
        return Comment_Notification_on_SharedPosts.objects.filter(commented=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response('no comments', status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
        