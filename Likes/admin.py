from django.contrib import admin
from . models import *

admin.site.register(Like_SharedPosts)
admin.site.register(Like_WrittenPosts)
admin.site.register(Like_Notification_on_WrittenPosts)
admin.site.register(Like_Notification_on_SharedPosts)
