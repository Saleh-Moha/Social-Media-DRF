from rest_framework.permissions import BasePermission, SAFE_METHODS

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
            return not obj.is_private or obj.id == request.user.id
        # Write permissions are only allowed for the owner of the object
        return obj.id == request.user.id
    
class IsOnlyOwenr(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Requesting user can read their own follow requests
        if request.method in SAFE_METHODS:
            return obj.requested == request.user
        # Only the requested user can update or delete the follow request
        return obj.requested == request.user

    
