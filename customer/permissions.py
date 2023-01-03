from rest_framework import permissions

from customer.models import Customer

class CustomersPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        for i in Customer.objects.all():
            if str(request.user) == str(i.first_name+" "+i.last_name):
                return True
        return False
