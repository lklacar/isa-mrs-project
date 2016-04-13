from __future__ import unicode_literals

from django.db import models

# Create your models here.
from authentication.models import AbstractUser


class Guest(AbstractUser):
    pass
