from django.db import models

# Create your models here.
class UserInfo(models.Model):
    user_type_choices = (
        (1,'basic'),
        (2,'vip'),
        (3,'admin'),
    )
    user_type = models.IntegerField(choices=user_type_choices)
    user_name = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=64)

class UserToken(models.Model):
    user = models.OneToOneField(to='UserInfo',on_delete=models.CASCADE)
    token = models.CharField(max_length=64)


class House(models.Model):
    status_code_choices = (
        (1, 'working'),
        (2, 'standby'),
        (3, 'malfunction')
    )
    house_id = models.IntegerField(primary_key=True)
    house_name = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=32)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude =models.FloatField()
    created_date = models.DateField(auto_now=True)
    status_code = models.IntegerField(choices=status_code_choices)
    def __str__(self):
        return self.house_name
    class Meta:
        db_table = 'house'

class Thing(models.Model):
    status_code_choices = (
        (1, 'working'),
        (2, 'standby'),
        (3, 'malfunction')
    )
    thing_id = models.IntegerField(primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    position_x = models.FloatField()
    position_y = models.FloatField()
    cpu_temp = models.FloatField()
    fan_flag = models.BooleanField(default=True)
    status_code = models.IntegerField(choices=status_code_choices)
    created_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.thing_id
    class Meta:
        db_table = 'thing'

class Sensor(models.Model):
    status_code_choices = (
        (1, 'working'),
        (2, 'standby'),
        (3, 'malfunction')
    )
    sensor_ucode = models.CharField(max_length=64, unique=True)
    sensor_name = models.CharField(max_length=64, unique=True)
    sensor_type = models.ForeignKey('SensorType', on_delete=models.CASCADE)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    unit = models.CharField(max_length=32)
    precision_percent = models.FloatField()
    min_value = models.FloatField()
    max_value = models.FloatField()
    maker = models.CharField(max_length=64)
    model_code = models.CharField(max_length=64)
    status_code = models.IntegerField(choices=status_code_choices)
    used_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.sensor_name
    class Meta:
        db_table = 'sensor'

class SensorValue(models.Model):
    sensor_value = models.FloatField(null=False)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    unit = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'sensorvalue'

class SensorType(models.Model):
    type_name = models.CharField(max_length=64)
    class Meta:
        db_table = 'sensortype'

class Machine(models.Model):
    status_code_choices = (
        (1, 'working'),
        (2, 'standby'),
        (3, 'malfunction')
    )
    machine_id = models.IntegerField(primary_key=True)
    machine_name = models.CharField(max_length=64, unique=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    maker = models.CharField(max_length=64)
    model_code = models.CharField(max_length=64)
    ele_consumption = models.FloatField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    status_code = models.IntegerField(choices=status_code_choices)
    created_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.machine_name
    class Meta:
        db_table = 'machine'

class MachineType(models.Model):
    type_name = models.CharField(max_length=64)
    class Meta:
        db_table = 'machinetype'