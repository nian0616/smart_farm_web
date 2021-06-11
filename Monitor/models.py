from django.db import models

class Monitor_video(models.Model):
    name = models.CharField(max_length = 10)
    path = models.CharField(max_length = 100)
    time = models.DateTimeField("time published")

class Environment_monitor(models.Model):
    temp = models.FloatField(default = 0)
    light_intensity = models.FloatField(default = 0)
    CO_concentration = models.FloatField(default = 0)
    humidity = models.FloatField(default = 0)
    soil_humidity = models.FloatField(default = 0)
    precipitation = models.FloatField(default = 0)
    time = models.DateTimeField("time published")

class Crop_maturity(models.Model):
    crop_name = models.CharField(max_length = 10)
    maturity = models.FloatField(default = 0)
    time = models.DateTimeField("time published")