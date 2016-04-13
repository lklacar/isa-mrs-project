from django.contrib import admin

# Register your models here.
from friendship.models import Friend

from guest.models import Guest

admin.site.register(Guest)
