from __future__ import unicode_literals

# Create your models here.
from authentication.models import User


class SystemManager(User):
    def role(self):
        return "system_manager"
