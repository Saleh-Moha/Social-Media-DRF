from rest_framework import generics
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
from .permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import NotAuthenticated



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