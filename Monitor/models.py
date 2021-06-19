from django.db import models
from django.utils import timezone

class Monitor_video(models.Model):
    name = models.CharField(max_length = 10, default = '')
    path = models.CharField(max_length = 100, default = '')
    time = models.DateTimeField(default = timezone.now)

class Environment_monitor(models.Model):
    temp = models.FloatField(default = 0)
    light_intensity = models.FloatField(default = 0)
    CO_concentration = models.FloatField(default = 0)
    humidity = models.FloatField(default = 0)
    soil_humidity = models.FloatField(default = 0)
    precipitation = models.FloatField(default = 0)
    year = models.IntegerField(default = 0)
    month = models.IntegerField(default = 0)
    day = models.IntegerField(default = 0)
    hour = models.IntegerField(default = 0)