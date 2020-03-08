"""
Definition of models.
"""

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'male'),
        ('female', 'female')
    ))

class Order(models.Model):
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=(
        ('male', 'male'),
        ('female', 'female')
    ))
    gender_preferences = models.CharField(max_length=10, choices=(
        ('male', 'male'),
        ('female', 'female'),
        ('no matter', 'no matter')
    ))
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())
    room_url = models.TextField(max_length=500)
