from rest_framework import permissions

from .models import Seller

class SellerPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        for i in Seller.objects.all():
            if str(request.user) == str(i.email+" "+i.first_name+" "+i.last_name):
                return True
        return False