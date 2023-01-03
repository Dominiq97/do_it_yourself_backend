from rest_framework import permissions

from administrator.models import Administrator

class AdministratorsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        for i in Administrator.objects.all():
            if str(request.user) == str(i.first_name+" "+i.last_name):
                return True
        return False