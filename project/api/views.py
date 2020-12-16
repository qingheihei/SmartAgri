import json
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.views import APIView
from rest_framework.authentication import BaseAuthentication,BasicAuthentication
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer,AdminRenderer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from api import models
from api.utils.permission import AdminPermission
from api.utils.serializer import *
from api.utils.customize_pagination import *
from api.utils.filter import *


# Create your views here.

def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

class AuthView(APIView):
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        ret = {
            'code': '1000',
            'msg': 'None'
        }
        try:
            user = request._request.POST.get('user_name')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(user_name=user,password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "user error"
            token = md5(user)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = 'eee'
        return JsonResponse(ret)


@method_decorator(csrf_exempt, name='dispatch')
class HouseView(ModelViewSet):
    queryset = models.House.objects.all()
    serializer_class = HouseSerializer
    pagination_class = MyPageNumberPagination
    filter_class = HouseFilter

class ThingView(ModelViewSet):
    queryset = models.Thing.objects.all()
    serializer_class = ThingSerializer
    pagination_class = MyPageNumberPagination
    filter_class = ThingFilter

class SensorView(ModelViewSet):
    queryset = models.Sensor.objects.all()
    serializer_class = SensorSerializer
    pagination_class = MyPageNumberPagination
    filter_class = SensorFilter
  
class SensorValueView(ModelViewSet):
    queryset = models.SensorValue.objects.all()
    serializer_class = SensorValueSerializer
    pagination_class = MyPageNumberPagination
    filter_class = SensorValueFilter

class SensorTypeView(ModelViewSet):
    queryset = models.SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    pagination_class = MyPageNumberPagination
    filter_class = SensorTypeFilter

class MachineView(ModelViewSet):
    queryset = models.Machine.objects.all()
    serializer_class = MachineSerializer
    pagination_class = MyPageNumberPagination

class MachineTypeView(ModelViewSet):
    queryset = models.MachineType.objects.all()
    serializer_class = MachineTypeSerializer
    pagination_class = MyPageNumberPagination