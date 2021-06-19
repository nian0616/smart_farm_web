from django.db import models
from django.utils import timezone

class Crop_maturity(models.Model):
    crop_name = models.CharField(max_length = 10, default = '')
    maturity = models.FloatField(default = 0)
    time = models.DateTimeField(default = timezone.now)