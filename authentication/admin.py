from django.contrib import admin

# Register your models here.
from authentication.models import GenericUser

admin.site.register(GenericUser)
