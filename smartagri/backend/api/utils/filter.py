import django_filters
from django_filters import rest_framework as filters
from api import models

class SensorValueFilter(filters.FilterSet):
    from_date = filters.DateTimeFilter(field_name="created_at",lookup_expr='gt')
    until_date = filters.DateTimeFilter(field_name="created_at",lookup_expr='lt')
    sensor_type = filters.CharFilter(field_name='sensor__sensor_type__type_name',lookup_expr='icontains')
    class Meta:
        model = models.SensorValue
        fields = ['from_date','until_date','sensor_type']

class OperationFilter(filters.FilterSet):
    device_type = filters.CharFilter(field_name='device__device_type__type_name',lookup_expr='icontains')
    user_name = filters.CharFilter(field_name='user__name',lookup_expr='icontains')
    from_date = filters.DateTimeFilter(field_name="created_at",lookup_expr='gt')
    until_date = filters.DateTimeFilter(field_name="created_at",lookup_expr='lt')
    class Meta:
        model = models.Operation
        fields = ['from_date','until_date','device_type','user_name']