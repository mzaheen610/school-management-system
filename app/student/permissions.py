"""
Permissions for different user types.
"""

from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Permission class for admin users."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsSchoolStaff(BasePermission):
    """Permission class for school staff users."""
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_school_staff


class IsParent(BasePermission):
    """Permission class for parent users."""
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_parent:
            print("True")
        else:
            print("False")
        print(request.user.is_parent)
        return request.user and request.user.is_authenticated and request.user.is_parent

