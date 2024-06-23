from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user-profile/<int:pk>', User_Profile.as_view()),
    path('user-profile-info/<int:pk>', User_Profile_Info.as_view()),
    path('do-follow/<int:id>', Do_Follow.as_view()),
    path('follow-request/<int:pk>', FollowRequest.as_view()),
    path('followers', Followers.as_view()),
    path('followings', Following.as_view()),
]
