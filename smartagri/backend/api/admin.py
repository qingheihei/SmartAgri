from django.contrib import admin
from .models import Sensor,SensorType
# Register your models here.

admin.site.register([Sensor,SensorType])
