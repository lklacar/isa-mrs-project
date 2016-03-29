from __future__ import unicode_literals

from django.db import models

# Create your models here.
from restaurant.models import Food, Drink


class Order(models.Model):
    total_price = models.DecimalField(max_digits=5, decimal_places=2)

    def drinks(self):
        return SingleDrinkOrder.objects.filter(order=self)

    def food(self):
        return SingleFoodOrder.objects.filter(s=self)


class SingleOrder(models.Model):
    order = models.ForeignKey(Order)
    single_price = models.IntegerField()
    quantity = models.IntegerField()

    class Meta:
        abstract = True


class SingleFoodOrder(SingleOrder):
    item = models.ForeignKey(Food)


class SingleDrinkOrder(SingleOrder):
    item = models.ForeignKey(Drink)
