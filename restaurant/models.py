from __future__ import unicode_literals
from django.db import models

# Create your models here.
from authentication.models import User
from manager.models import Manager


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    manager = models.OneToOneField(Manager)


class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant)


class Drink(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant)
