from django.contrib import admin

# Register your models here.
from employee.models import Waiter, Chef, Bartender

admin.site.register(Waiter)
admin.site.register(Chef)
admin.site.register(Bartender)
