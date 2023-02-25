from rest_framework.permissions import BasePermission
from ads.models import User


class IsOwner(BasePermission):
    message = 'You do not have permission to delete an selection'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False


class IsOwnerOrStaff(BasePermission):
    message = 'You do not have permission to delete an ad'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author_id or request.user.role in [User.admin, User.moderator]:
            return True
        return False
