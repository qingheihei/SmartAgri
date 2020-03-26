from rest_framework import serializers
from api import models

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SensorType
        fields = "__all__"
        depth = 1
    def create(self, validated_data):
        id = validated_data['type_id']
        name = validated_data['type_name']
        sensortype = models.SensorType.objects.create(type_id=id, type_name=name)
        return sensortype

class SensorSerializer(serializers.ModelSerializer):
    sensor_type = serializers.CharField(source="sensor_type.type_name", read_only=True)
    sensor_type_id = serializers.PrimaryKeyRelatedField(queryset=models.SensorType.objects.all(), write_only=True)
    class Meta:
        model = models.Sensor
        fields = ['ucode','name','status','x_coord','y_coord','sensor_type','sensor_type_id','created_at']
        extra_kwargs = {'x_coord':{'write_only':True},'y_coord':{'write_only':True},'updated_at': {'read_only': True},'created_at': {'read_only': True}}
    def create(self, validated_data):
        sensor_type = validated_data.pop('sensor_type_id')
        sensor = models.Sensor.objects.create(sensor_type=sensor_type, **validated_data)
        return sensor

class SensorValueSerializer(serializers.ModelSerializer):
    sensor_name = serializers.CharField(source="sensor.name", read_only=True)
    sensor_id = serializers.PrimaryKeyRelatedField(queryset=models.Sensor.objects.all(), write_only=True)
    class Meta:
        model = models.SensorValue
        fields = ['value','sensor_name','sensor_id','unit','created_at']
    def create(self, validated_data):
        sensor = validated_data.pop('sensor_id')
        sensor_value = models.SensorValue.objects.create(sensor=sensor, **validated_data)
        return sensor_value
     
class DeviceSerializer(serializers.ModelSerializer):
    device_type = serializers.CharField(source="device_type.type_name")
    class Meta:
        model = models.Device
        fields = ['ucode','status','device_type']

class OperationSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.name", read_only=True)
    device_code = serializers.CharField(source="device.ucode", read_only=True)
    device_id = serializers.PrimaryKeyRelatedField(queryset=models.Device.objects.all(), write_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=models.User.objects.all(), write_only=True)
    class Meta:
        model = models.Operation
        fields = ['device_code','device_id','user_name','user_id','new_state','created_at']
    def create(self, validated_data):
        device = validated_data.pop('device_id')
        user = validated_data.pop('user_id')
        sensor_value = models.Operation.objects.create(device=device,user=user, **validated_data)
        return sensor_value

class CameraSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Camera
        fields = "__all__"

# TBD
class ImageSerializer(serializers.ModelSerializer):
    camera_id = serializers.PrimaryKeyRelatedField(queryset=models.Camera.objects.all(), write_only=True)  
    class Meta:
        model = models.Image
        fields = ['camera_id','img_path','created_at']
        #fields = "__all__"
    def create(self, validated_data):
        print("********"),validated_data
        camera = validated_data.pop('camera_id')
        image = models.Image.objects.create(camera=camera, **validated_data)
        return image
    def get_image_url(self, image):
            request = self.context.get('request')
            if image and hasattr(image, 'url'):
               img_path = image.img_path.url
               return request.build_absolute_uri(img_path)
            else:
               return None

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}