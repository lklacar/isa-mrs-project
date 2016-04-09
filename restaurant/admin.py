from django.contrib import admin

# Register your models here.
from restaurant.models import Restaurant, Food, Drink

admin.site.register(Restaurant)
admin.site.register(Food)
admin.site.register(Drink)
