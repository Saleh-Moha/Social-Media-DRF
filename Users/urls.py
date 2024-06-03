from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('user-profile/<str:username>', User_Profile.as_view()),
]