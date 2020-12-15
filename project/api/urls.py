from django.conf.urls import url,include
from . import views

urlpatterns = [
    #url(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
    
    url(r'^auth/$', views.AuthView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/houses/(?P<id>\d+)$', views.HouseView.as_view(),name='hs'),
    url(r'^(?P<version>[v1|v2]+)/sensors/', views.SensorView.as_view()),
    url(r'^(?P<version>[v1|v2]+)/things/', views.ThingView.as_view()),
]