from manager.models import Manager
from seeding.seeds.abstract_seed import AbstractSeed


class ManagerSeed(AbstractSeed):
    def seed(self):
        manager = Manager()
        manager.email = "vinokicmiljana@gmail.com"
        manager.set_password("genius94")
        manager.first_name = "Miljana"
        manager.last_name = "Vinokic Klacar"
        manager.is_staff = False
        manager.is_superuser = False
        manager.is_confirmed = True
        manager.save()
