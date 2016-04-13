from authentication.models import AbstractUser
from seeding.seeds.abstract_seed import AbstractSeed
from system_manager.models import SystemManager


class SystemManagerSeed(AbstractSeed):
    def seed(self):
        system_manager = SystemManager()
        system_manager.role = "SYSTEM_MANAGER"
        system_manager.email = "systemmanager@example.com"
        system_manager.set_password('password')
        system_manager.first_name = "System Manager"
        system_manager.last_name = "Example"
        system_manager.is_active = True
        system_manager.is_confirmed = True
        system_manager.is_staff = False
        system_manager.is_superuser = False

        system_manager.save()
