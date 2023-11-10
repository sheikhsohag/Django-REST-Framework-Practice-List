from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method == 'POST':
            return True
        if request.method == 'DELETE':
            return True
        return False