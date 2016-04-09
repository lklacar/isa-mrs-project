from django.contrib import admin

from manager.models import Manager
from restaurant.models import Menu

admin.site.register(Manager)
admin.site.register(Menu)
