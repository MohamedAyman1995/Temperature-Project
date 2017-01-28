from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Weather (models.Model) :
    temprature = models.FloatField(default=None,validators=[MaxValueValidator(28), MinValueValidator(19)])
    humidity   = models.FloatField(default=None,validators=[MaxValueValidator(65), MinValueValidator(35)])
    date = models.DateTimeField(default=datetime.now)
