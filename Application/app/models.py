"""
Definition of models.
"""

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    location = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())
