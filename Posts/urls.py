from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('post', WritePosts.as_view()),
    path('post-list/<int:id>', Written_posts_list.as_view()),
    path('edit-post/<int:pk>', EditWrittenPosts.as_view()),
    path('<str:username>/<int:id>/share', SharePosts.as_view()),
    path('sharepost-list/<int:id>', Shared_posts_list.as_view()),
    path('edit-sharedpost/<int:pk>', EditSharedPosts.as_view()),
]