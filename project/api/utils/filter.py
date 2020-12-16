from django_filters import rest_framework as filters
from api import models

class HouseFilter(filters.FilterSet):
    city = filters.CharFilter(field_name="city", lookup_expr="contains")
    status = filters.CharFilter(field_name="status_code", method='status_filter')
    def status_filter(self, queryset, name, value):
        status_map = {code: status for status, code in models.House.status_code_choices}
        code = status_map[value]
        return queryset.filter(status_code=code)
    class Meta:
        model = models.House
        fields = ['city','status']

class ThingFilter(filters.FilterSet):
    house = filters.CharFilter(field_name='house__house_name',lookup_expr='icontains')
    house_id = filters.NumberFilter(field_name='house__house_id')
    status = filters.CharFilter(field_name="status_code", method='status_filter')
    since = filters.DateTimeFilter(field_name="created_date",lookup_expr='gte')
    def status_filter(self, queryset, name, value):
        status_map = {code: status for status, code in models.Thing.status_code_choices}
        code = status_map[value]
        return queryset.filter(status_code=code)
    class Meta:
        model = models.Thing
        fields = ['house','house_id', 'status','since']

class SensorFilter(filters.FilterSet):
    thing_id = filters.NumberFilter(field_name='thing__thing_id')
    sensor_type = filters.CharFilter(field_name='sensor_type__type_name')
    status = filters.CharFilter(field_name="status_code", method='status_filter')
    def status_filter(self, queryset, name, value):
        status_map = {code: status for status, code in models.Sensor.status_code_choices}
        code = status_map[value]
        return queryset.filter(status_code=code)
    class Meta:
        model = models.Sensor
        fields = ['thing_id','sensor_type', 'status']

class SensorValueFilter(filters.FilterSet):
    sensor = filters.CharFilter(field_name='sensor__sensor_name',lookup_expr='icontains')
    sensor_ucode = filters.CharFilter(field_name='sensor__sensor_ucode')
    sensor_type = filters.CharFilter(field_name='sensor__sensor_type__type_name')
    since = filters.DateTimeFilter(field_name="created_at",lookup_expr='gte')
    until = filters.DateTimeFilter(field_name="created_at",lookup_expr='lte') # 00:00:00 default
    class Meta:
        model = models.SensorValue
        fields = ['sensor','sensor_ucode','sensor_type','since','until']

class SensorTypeFilter(filters.FilterSet):
    type = filters.CharFilter(field_name='type_name')
    class Meta:
        model = models.SensorType
        fields = ['type']