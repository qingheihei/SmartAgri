from django.conf.urls import url,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'houses', views.HouseView)
router.register(r'things', views.ThingView)
router.register(r'sensors', views.SensorView)
router.register(r'sensorvalues', views.SensorValueView)
router.register(r'sensortypes', views.SensorTypeView)
router.register(r'machines', views.MachineView)
router.register(r'machinetypes', views.MachineTypeView)

urlpatterns = [
    url(r'^auth/$', views.AuthView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
]