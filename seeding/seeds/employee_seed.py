from employee.models import Waiter, Bartender, Chef
from restaurant.models import Restaurant
from seeding.seeds.abstract_seed import AbstractSeed


class WaiterSeed(AbstractSeed):
    def seed(self):
        waiter = Waiter()
        waiter.role = "WAITER"
        waiter.email = "kristina@kolosek.com"
        waiter.set_password("gazerocker")
        waiter.first_name = "Kristina"
        waiter.last_name = "Grujic"
        waiter.is_staff = False
        waiter.is_superuser = False
        waiter.is_confirmed = True
        waiter.works_in = Restaurant.objects.get(id=1)
        waiter.save()
