from rest_framework.permissions import BasePermission

from ads.models import User


class AdCreatePermission(BasePermission):
    message = 'You do not have permission to create an ad'

    def has_permission(self, request, view):
        if request.user.role == User.admin or User.moderator:
            return True
        return False


class AdDeletePermission(BasePermission):
    message = 'You do not have permission to create an ad'

    def has_permission(self, request, view):
        if request.user.role == User.admin or User.moderator:
            return True
        return False
