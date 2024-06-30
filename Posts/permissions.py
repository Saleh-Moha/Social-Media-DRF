from rest_framework.permissions import BasePermission, SAFE_METHODS
from Users.models import Follow
class IsOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        # Allow read-only access for any request (both authenticated and unauthenticated users)
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed for authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for any request
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed for the owner of the object
        return obj.user == request.user

class IsOwnerPrivate(BasePermission):
    
    def has_permission(self, request, view):
        # Allow read-only access for any request (both authenticated and unauthenticated users)
        if request.method in SAFE_METHODS:
            return True
        # Write permissions are only allowed for authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only access for any request if the user is the owner or a follower
        if request.method in SAFE_METHODS:
            if request.user.is_authenticated:
                return (not obj.is_private or obj.user.id == request.user.id or 
                        Follow.objects.filter(follower=request.user, followed=obj.user).exists())
            else:
                return not obj.is_private
        # Write permissions are only allowed for the owner of the object
        return obj.user.id == request.user.id
