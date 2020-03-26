from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import exceptions
from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from . import models
from rest_framework import serializers
import json
from api.utils.serializer import *
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from api.utils.customize_viewset_base import CustomizeViewBase
import os
from rest_framework import status

IMAGE_DIR = 'media/image/'

class MyPageNumberPagination(CursorPagination):
    #page_size = 2
    #page_size_query_param = "size"
    #max_page_size = 10
    #page_query_param = "page"
    #default_limit = 2
    #limit_query_param = 'limit'
    #offset_query_param = 'offset'
    #max_limit = 10
    cursor_query_param = "cursor"
    page_size = 2
    ordering = "id"
    max_page_size = 10


from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer,AdminRenderer
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet

class SensorView(CustomizeViewBase):
    queryset = models.Sensor.objects.all()
    serializer_class = SensorSerializer


from django.views import View
from .utils.filter import SensorValueFilter,OperationFilter
@method_decorator(csrf_exempt, name='dispatch')
class SensorValueView(CustomizeViewBase):
    queryset = models.SensorValue.objects.all()
    serializer_class = SensorValueSerializer
    panination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = SensorValueFilter

class SensorTypeView(CustomizeViewBase):
    queryset = models.SensorType.objects.all()
    serializer_class = SensorTypeSerializer
    panination_class = PageNumberPagination

class DeviceView(CustomizeViewBase):
    queryset = models.Device.objects.all()
    serializer_class = DeviceSerializer
    panination_class = PageNumberPagination

class OperationView(CustomizeViewBase):
    queryset = models.Operation.objects.all()
    serializer_class = OperationSerializer
    panination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = OperationFilter

class CameraView(CustomizeViewBase):
    queryset = models.Camera.objects.all()
    serializer_class = CameraSerializer
    panination_class = PageNumberPagination

class ImageView(CustomizeViewBase):
    queryset = models.Image.objects.all()
    serializer_class = ImageSerializer
    panination_class = PageNumberPagination

class UserView(ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer
    panination_class = PageNumberPagination

def md5(user):
    import hashlib
    import time
    #生成随机字符串
    ctime = str(time.time())
    m=hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()

class AuthView(APIView):
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        ret = {'code':1000, 'msg':None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            print(user, pwd)
            obj = models.User.objects.filter(name=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "wrong name or psd"
            token = md5(user)
            #存在就更新，不存在就创建
            ret1,ret2 = models.UserToken.objects.update_or_create(user=obj, defaults={'token':token})
            print(ret2)
            ret['token'] = token            
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = 'excep'
            print(e.__context__)

        return JsonResponse(ret)
