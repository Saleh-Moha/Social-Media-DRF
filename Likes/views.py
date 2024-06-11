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

class Likewrittenposts(generics.CreateAPIView):
    queryset = Like_WrittenPosts.objects.all()
    serializer_class = LikeWrittenPostsSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['id']
        try:
            post = Written_Posts.objects.get(id=post_id)
        except Written_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Like_WrittenPosts.objects.filter(user=user, post=post).exists():
            return Response({"detial":"you have already liked it"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(user=user, post=post)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        
        
        
class Likesharedposts(generics.CreateAPIView):
    queryset = Like_SharedPosts.objects.all()
    serializer_class = LikeSharedPostsSerializers
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = self.request.user
        post_id = self.kwargs['id']
        try:
            post = Shared_Posts.objects.get(id=post_id)
        except Shared_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if Like_SharedPosts.objects.filter(user=user, post=post).exists():
            return Response({"detial":"you have already liked it"},status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save(user=user, post=post)
            return Response(serializer.data,status=status.HTTP_201_CREATED)




class Like_writtenpost_list(generics.ListAPIView):
    queryset = Like_WrittenPosts.objects.all()
    serializer_class = LikeWrittenPostsSerializers
    
    def get_queryset(self):
        post_id = self.kwargs['id']
        try:
            post =  Written_Posts.objects.get(id=post_id)
        except Written_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Like_WrittenPosts.objects.filter(post=post)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count() 
        if not queryset.exists():
            return Response('no likes for this item',status=status.HTTP_404_NOT_FOUND)
        if count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset,many=True)
        
        data = {'count': count,
                'data':serializer.data}
        serializer = LikeCountWrittenpostsSerializer(data)
        return Response(serializer.data)
    
    
    
class Like_sharedpost_list(generics.ListAPIView):
    queryset = Like_SharedPosts.objects.all()
    serializer_class = LikeSharedPostsSerializers
    
    def get_queryset(self):
        post_id = self.kwargs['id']
        try:
            post =  Shared_Posts.objects.get(id=post_id)
        except Shared_Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Like_SharedPosts.objects.filter(post=post)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        count = queryset.count() 
        if not queryset.exists():
            return Response('no likes for this item',status=status.HTTP_404_NOT_FOUND)
        if count == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(queryset,many=True)
        
        data = {'count': count,
                'data':serializer.data}
        serializer = LikeCountSharedpostsSerializer(data)
        return Response(serializer.data)


class Like_Delete_writtenpost(generics.DestroyAPIView):
    queryset = Like_WrittenPosts.objects.all()
    serializer_class = LikeWrittenPostsSerializers
    permission_classes = [IsOwnerOrReadOnly]




class Like_Delete_sharedposts(generics.DestroyAPIView):
    queryset = Like_SharedPosts.objects.all()
    serializer_class = LikeSharedPostsSerializers
    permission_classes = [IsOwnerOrReadOnly]
