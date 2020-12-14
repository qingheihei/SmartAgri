from django.contrib import admin
from .models import House,Thing,Sensor,Machine

# Register your models here.
admin.site.register(House)
admin.site.register(Thing)
admin.site.register(Sensor)
