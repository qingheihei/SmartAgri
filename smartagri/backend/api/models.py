from django.db import models
from django.conf import settings 

# Create your models here.
class Sensor(models.Model):
    ucode = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=32,)
    sensor_type = models.ForeignKey('SensorType', on_delete=models.CASCADE)
    status = models.BooleanField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    is_deleted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'sensor'

class SensorType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=64)
    class Meta:
        db_table = 'sensortype'

class SensorValue(models.Model):
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE)
    value = models.FloatField()
    unit = models.CharField(max_length=20,)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'sensorvalue'

class Device(models.Model):
    ucode = models.CharField(max_length=64, unique=True)
    device_type = models.ForeignKey('DeviceType', on_delete=models.CASCADE)
    status = models.BooleanField()
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    class Meta:
        db_table = 'device'
    def __str__(self):
        return '%s'%(self.ucode)

class DeviceType(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=64)
    class Meta:
        db_table = 'devicetype'
    def __str__(self):
        return '%s'%(self.type_name)

class Operation(models.Model):
    device = models.ForeignKey('Device', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    new_state = models.BooleanField()
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'operation'

class Camera(models.Model):
    ucode = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    status = models.BooleanField()
    class Meta:
        db_table = 'camera'

class Image(models.Model):
    camera = models.ForeignKey('Camera', on_delete=models.CASCADE)
    img_path = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'image'
    def __str__(self):
        return '{}'.format(self.img_path)

class User(models.Model):
    user_type_choices = (
        (1,'usual'),
        (2,'vip'),
        (3,'admin'),
    )
    type = models.IntegerField(choices=user_type_choices)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    stu_code = models.CharField(max_length=32,unique=True)
    stu_mail = models.CharField(max_length=64,unique=True)
    class Meta:
        db_table = 'user'
    def __str__(self):
        return '%s'%(self.name)

class UserToken(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=64)
    valid_to = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'usertoken'
