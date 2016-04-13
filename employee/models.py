from __future__ import unicode_literals

from django.db import models

# Create your models here.
from authentication.models import AbstractUser

from restaurant.models import Restaurant


class Employee(AbstractUser):
    shoe_size = models.CharField(max_length=10, default=0)
    clothes_size = models.CharField(max_length=10, default=0)
    works_in = models.ForeignKey(Restaurant, default=None)
    password_change_count = models.IntegerField(default=0)

    CHOICES = (
        ("WAITER", 'Waiter'),
        ("CHEF", 'Chef'),
        ("BARTENDER", 'Bartender'),
    )
    role = models.CharField(max_length=20,
                            choices=CHOICES,
                            default="WAITER")
