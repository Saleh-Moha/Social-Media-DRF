from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('comment-written-post/<int:id>', Commentwrittenposts.as_view()),
    path('comment-written-post-list/<int:id>', Comment_writtenpost_list.as_view()),
    path('comment-written-post-delete/<int:pk>', Comment_Delete_writtenpost.as_view()),
    path('comment-shared-post/<int:id>', Commentsharedposts.as_view()),
    path('comment-shared-post-list/<int:id>', Comment_sharedpost_list.as_view()),
    path('comment-shared-post-delete/<int:pk>', Comment_Delete_sharedposts.as_view()),
    path('written-posts-comment-notification', Written_Posts_Comments_Notification.as_view()),
    path('shared-posts-comment-notification', Shared_Posts_Comments_Notification.as_view()),
]