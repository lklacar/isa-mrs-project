import names

from manager.models import Manager
from seeding.seeds.abstract_seed import AbstractSeed


class ManagerSeed(AbstractSeed):
    def seed(self):
        for i in range(10):
            first_name = names.get_first_name()
            last_name = names.get_full_name()

            guest = Manager()
            guest.role = "GUEST"
            guest.email = "manager%s@example.com" % str(i)
            guest.set_password('password')
            guest.first_name = first_name
            guest.last_name = last_name
            guest.is_active = True
            guest.is_confirmed = True
            guest.is_staff = False
            guest.is_superuser = False

            guest.save()
