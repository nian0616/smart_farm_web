from django.db import models

class Face_image(models.Model):
    name = models.CharField(max_length = 10)
    path = models.CharField(max_length = 100)
    time = models.DateTimeField("time published")
