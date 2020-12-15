from django.conf.urls import url,include
from api.utils.serializer import *
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'sensorvalues', views.SensorValueView)

urlpatterns = [
    #url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
    
    url(r'^auth/$', views.AuthView.as_view()),
    #url(r'^(?P<version>[v1|v2]+)/houses/(?P<id>\d+)$', views.HouseView.as_view(),name='hs'),
    url(r'^(?P<version>[v1|v2]+)/houses/$', views.HouseView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/sensors/$', views.SensorView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/sensortypes/$', views.SensorTypeView.as_view()),

    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
    # url(r'^(?P<version>[v1|v2]+)/sensorvalues/$', views.SensorValueView.as_view({'get': 'list','post': 'create'})),
    # url(r'^(?P<version>[v1|v2]+)/sensorvalues\.(?P<format>\w+)$', views.SensorValueView.as_view({'get': 'list','post': 'create'})),
    # url(r'^(?P<version>[v1|v2]+)/sensorvalues/(?P<pk>\d+)$', views.SensorValueView.as_view({'get': 'retrieve','delete': 'destroy','put': 'update','patch': 'partial_update'})),
    # url(r'^(?P<version>[v1|v2]+)/sensorvalues\.(?P<format>\w+)$', views.SensorValueView.as_view({'get': 'retrieve','delete': 'destroy','put': 'update','patch': 'partial_update'})),
    
    url(r'^(?P<version>[v1|v2]+)/things/$', views.ThingView.as_view()),
]