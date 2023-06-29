from django.db import models

# Create your models here.
from django.db import models

class FitnessProfile(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    goal = models.IntegerField()
    activity_level = models.IntegerField()
    time_commitment = models.IntegerField()
    calorie_target = models.IntegerField()
    protein = models.IntegerField()
    carbs = models.IntegerField()
    fats = models.IntegerField()
    program = models.CharField(max_length=255)
