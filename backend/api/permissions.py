from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions


class CreatePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == AnonymousUser:
            return False
        return (request.user.role == 'admin')


class PutPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == AnonymousUser:
            return False
        return (request.user.role == 'admin')


class DeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user == AnonymousUser:
            return False
        return bool(request.user.role == 'boss')
