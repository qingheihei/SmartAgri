from rest_framework import serializers
from api import models


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.House
        fields = "__all__"

class ThingSerializer(serializers.ModelSerializer):
    ooo = serializers.CharField(source="get_status_code_display")
    class Meta:
        model = models.Thing
        fields = ['thing_id','house','cpu_temp','ooo']
        depth = 1

class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorValue
        fields = "__all__"

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorType
        fields = "__all__"