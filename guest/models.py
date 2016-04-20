from __future__ import unicode_literals

from django.db import models

from authentication.models import ConfirmationToken, AbstractUser


class Guest(AbstractUser):
    confirmation_token = models.OneToOneField(ConfirmationToken, blank=True, default=None, null=True)