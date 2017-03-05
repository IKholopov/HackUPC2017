from django.db import models
from django.contrib.auth.admin import User

class Activity(models.Model):
    social_status_id = models.IntegerField(unique=False)
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    source = models.CharField(max_length=1024)
    score = models.FloatField(default=-1)
    geodata = models.CharField(max_length=128, null=True)

    @classmethod
    def create(cls, social_status_id, user_id, source, score, geodata):
        activity = Activity(social_status_id=social_status_id,user_id=user_id, source=source, score=score,
                            geodata=geodata)
        return activity
