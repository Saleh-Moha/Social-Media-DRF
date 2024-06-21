from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Posts.urls')),
    path('api/',include('Likes.urls')),
    path('api/',include('Comments.urls')),
    path('api/',include('Users.urls')),
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.authtoken')),
]