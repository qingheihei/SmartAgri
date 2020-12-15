from rest_framework import serializers
from api import models


class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thing
        fields = ['thing_id','house','cpu_temp','ooo']
        depth = 1

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorType
        fields = "__all__"