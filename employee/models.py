from __future__ import unicode_literals

from django.db import models

# Create your models here.
from authentication.models import User
from restaurant.models import Restaurant


class Employee(User):
    shoe_size = models.CharField(max_length=10)
    clothes_size = models.CharField(max_length=10)
    works_in = models.ForeignKey(Restaurant)


class Waiter(Employee):
    pass


class Chef(Employee):
    pass


class Bartender(Employee):
    pass
