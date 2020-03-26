from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from .. import models

class MyAuthentication(BaseAuthentication):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('auth failed')
        return(token_obj.user, token_obj)
    def authenticate_header(self, request):
        pass
