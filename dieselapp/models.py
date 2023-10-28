from django.contrib.auth.models import AbstractUser
from django.db import models


class DieselData(models.Model):
    """diesel data model"""
    generator_id = models.CharField(max_length=50)
    fuel_level = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.generator_id} {self.fuel_level} {self.timestamp}"
    
    def __repr__(self):
        return f"{self.generator_id} {self.fuel_level} {self.timestamp}"