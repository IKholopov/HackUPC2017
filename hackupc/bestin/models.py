from django.db import models

class Activity(models.Model):
    source = models.CharField(max_length=1024)
    score = models.IntegerField(default=-1)
