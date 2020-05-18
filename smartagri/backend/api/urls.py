from django.conf.urls import url,include
from rest_framework import routers
from rest_framework.request import Request
from . import views

router = routers.DefaultRouter()
router.register(r'sensors', views.SensorView)
router.register(r'sensorvalues', views.SensorValueView)
router.register(r'sensortypes', views.SensorTypeView)
router.register(r'devices', views.DeviceView)
router.register(r'operations', views.OperationView)
router.register(r'cameras', views.CameraView)
router.register(r'images', views.ImageView)
router.register(r'users', views.UserView)



urlpatterns = [
    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
    
    url(r'^auth/$', views.AuthView.as_view()),
]