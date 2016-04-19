from __future__ import unicode_literals
from django.db import models

# Create your models here.
from authentication.models import AbstractUser
from manager.models import Manager


class Menu(models.Model):
    pass


class RestaurantCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    manager = models.OneToOneField(Manager)
    menu = models.OneToOneField(Menu, blank=True, null=True)
    profile_image = models.ImageField(upload_to="static/upload/img")
    category = models.ForeignKey(RestaurantCategory, blank=True, default=None)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=5)
    menu = models.ForeignKey(Menu, blank=True, default=None)

    def __str__(self):
        return self.name


class Drink(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    menu = models.ForeignKey(Menu, blank=True, default=None)

    def __str__(self):
        return self.name


class Table(models.Model):
    number_of_seats = models.IntegerField()
    restaurant = models.ForeignKey(Restaurant)
    x = models.IntegerField()
    y = models.IntegerField()
