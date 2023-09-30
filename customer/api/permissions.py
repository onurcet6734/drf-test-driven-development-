from rest_framework.permissions import BasePermission
from customer.models import Customer

class NotAuthenticated(BasePermission):
    message = "You already have an account."
    
    def has_permission(self, request, view):
        return not request.user.is_authenticated
