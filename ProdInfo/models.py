from django.db import models

class Price(models.Model):
    name = models.CharField(max_length = 10)
    price = models.FloatField(default = 0)
    change_num = models.FloatField(default = 0)
    change_ratio = models.FloatField(default = 0)
    trading_volumes = models.FloatField(default = 0)
    pub_time = models.DateTimeField("time published")