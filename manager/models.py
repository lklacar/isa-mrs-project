from __future__ import unicode_literals

# Create your models here.



from authentication.models import AbstractUser


class Manager(AbstractUser):
    def role(self):
        return "MANAGER"
