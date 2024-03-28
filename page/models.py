from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=64, unique=True)
    studio = models.CharField(max_length=64, unique=True)
    release_date = models.DateField("date released")
