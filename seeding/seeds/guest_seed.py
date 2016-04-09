from authentication.models import User
from seeding.seeds.abstract_seed import AbstractSeed


class GuestSeed(AbstractSeed):
    def seed(self):
        for i in range(10):
            guest = User()
            guest.email = "guest%s@example.com" % str(i)
            guest.set_password('password')
            guest.first_name = "Guest %s" % str(i)
            guest.last_name = "Example"
            guest.is_active = True
            guest.is_confirmed = True
            guest.is_staff = False
            guest.is_superuser = False

            guest.save()
