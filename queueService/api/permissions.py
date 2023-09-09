from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ViewSet


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        print(type(request))
        print(type(view))
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff
