from django.db import models
from django.utils import timezone

class Face_image(models.Model):
    name = models.CharField(max_length = 10)
    path = models.CharField(max_length = 100)
    time = models.DateTimeField(default = timezone.now)
