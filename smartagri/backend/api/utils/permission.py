from rest_framework.permissions import BasePermission

class AdminPermission(BasePermission):
    def has_permission(self,request,view):
        print(request.user)
        if request.user.type !=3:
            return False
        return True