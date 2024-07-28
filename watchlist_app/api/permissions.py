from rest_framework import permissions

class IsAdminOrReadOnly(permissions.IsAdminUser):

    """
        This class applies a custom permission to access/edit info only by admin and rest can only read the info.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        else:
            bool(request.user and request.user.is_staff)


class IsReviewUserOrReadOnly(permissions.BasePermission):

    """
    This class lets only the reviewer edit the review info and rest can only read the info.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        else:
            return obj.review_user == request.user or request.user.is_staff