from rest_framework import serializers
from api import models

class SensorValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorValue
        fields = "__all__"

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorType
        fields = "__all__"

class SensorSerializer(serializers.ModelSerializer): ### 前10レコード表示？
    sensor_type = serializers.CharField(source='sensor_type.type_name')
    thing_id = serializers.CharField(source='thing.thing_id')
    status = serializers.CharField(source="get_status_code_display")
    class Meta:
        model = models.Sensor
        fields = ['sensor_ucode','sensor_name','sensor_type', 'thing_id', 'unit', 'precision_percent', 'min_value', 'max_value', 'maker', 'model_code', 'status', 'used_date']
        depth = 1

class ThingSerializer(serializers.ModelSerializer):
    house_id = serializers.CharField(source='house.house_id')
    status = serializers.CharField(source="get_status_code_display")
    sensors = SensorSerializer(many=True)
    class Meta:
        model = models.Thing
        fields = ['thing_id','house_id','sensors','cpu_temp', 'position_x', 'position_y', 'fan_flag', 'status', 'created_date']
        depth = 1

class MachineSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_code_display")
    class Meta:
        model = models.Machine
        fields = ['machine_id', 'machine_name', 'house_id', 'maker', 'model_code', 'ele_consumption', 'position_x', 'position_y', 'status', 'created_date']

class MachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MachineType
        fields = "__all__"

class HouseSerializer(serializers.ModelSerializer): ##simple version?
    things = ThingSerializer(many=True)
    machines = MachineSerializer(many=True)
    status = serializers.CharField(source="get_status_code_display")
    class Meta:
        model = models.House
        fields = ['house_id', 'house_name', 'things', 'city', 'address', 'latitude', 'longitude', 'status', 'created_date']
        depth = 0
