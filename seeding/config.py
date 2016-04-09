from seeding.seeds.admin_seed import AdminSeed
from seeding.seeds.guest_seed import GuestSeed
from seeding.seeds.manager_seed import ManagerSeed

SEEDS = {
    "admin": AdminSeed,
    "manager": ManagerSeed,
    "guest": GuestSeed,
}
