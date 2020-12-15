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
import json
from api import models
from api.utils.permission import AdminPermission
from api.utils.serializer import *
from api.utils.customize_pagination import *
from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser,FormParser
from rest_framework.viewsets import GenericViewSet


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
class HouseView(APIView):
    def get(self,request,*args,**kwargs):
        houses = models.House.objects.all()
        ser = HouseSerializer(instance=houses, many=True)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)

    def post(self,request,*args,**kwargs):
        print(request.data)
        return HttpResponse('POST OK')
    def put(self,request,*args,**kwargs):
        return HttpResponse('PUT OK')
    def delete(self,request,*args,**kwargs):
        return HttpResponse('DELETE OK')


class ThingView(APIView):
    def get(self,request,*args,**kwargs):
        things = models.Thing.objects.all()
        ser = ThingSerializer(instance=things, many=True,context={'request': request})
        #print(ser.data)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)

class MachineView(APIView):
    pass
class MachineTypeView(APIView):
    pass

class SensorView(APIView):
    #parser_classes = [JSONParser,FormParser,]
    def post(self,request,*args,**kwargs):
        #print(request.data)
        return HttpResponse('POST OK')
  
class SensorValueView(GenericViewSet):
    queryset = models.SensorValue.objects.all()
    serializer_class = SensorValueSerializer
    pagination_class = MyPageNumberPagination

    def list(self,request,*args,**kwargs):
        values = self.get_queryset()
        page_values = self.paginate_queryset(values)
        ser = self.get_serializer(instance=page_values, many=True)
        return Response(ser.data)
    def xxx(self,request,*args,**kwargs):
        return Response('xxx')


class SensorTypeView(APIView):
    def get(self,request,*args,**kwargs):
        #获取所有数据
        types = models.SensorType.objects.all()
        # 创建分页对象
        pg = MyPageNumberPagination()
        # 在数据库中获取分页的数据
        page_types = pg.paginate_queryset(queryset=types,request=request,view=self)
        # 对分页后的数据进行序列化
        ser = SensorTypeSerializer(instance=page_types, many=True)

        return pg.get_paginated_response(ser.data)

