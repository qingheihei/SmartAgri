from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self,request,view):
        print(request.user)
        if request.user.user_type <2:
            return False
        return True