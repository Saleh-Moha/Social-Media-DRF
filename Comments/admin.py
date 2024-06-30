from django.contrib import admin
from .models import *

admin.site.register(Comment_SharedPosts)
admin.site.register(Comment_WrittenPosts)
admin.site.register(Comment_Notification_on_WrittenPosts)
