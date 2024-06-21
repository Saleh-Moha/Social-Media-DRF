from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('like-written-post/<int:id>', Likewrittenposts.as_view()),
    path('like-written-post-list/<int:id>', Like_writtenpost_list.as_view()),
    path('like-written-post-delete/<int:pk>', Like_Delete_writtenpost.as_view()),
    path('like-shared-post/<int:id>', Likesharedposts.as_view()),
    path('like-shared-post-list/<int:id>', Like_sharedpost_list.as_view()),
    path('like-shared-post-delete/<int:pk>', Like_Delete_sharedposts.as_view()),
]