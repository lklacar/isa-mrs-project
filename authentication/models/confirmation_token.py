from django.db import models

from authentication.models import User


class ConfirmationToken(models.Model):
    user = models.OneToOneField(User)
    token = models.CharField(max_length=36)
    expires = models.DateTimeField()
