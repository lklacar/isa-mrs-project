from __future__ import unicode_literals

# Create your models here.

from authentication.models import User


class Manager(User):
    def role(self):
        return "manager"
