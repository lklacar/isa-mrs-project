from manager.models import Manager
from restaurant.models import Restaurant, Menu
from seeding.seeds.abstract_seed import AbstractSeed


class RestaurantSeed(AbstractSeed):
    def seed(self):
        restaurant = Restaurant()
        restaurant.name = "Example Restaurant"
        restaurant.description = "Example description"
        restaurant.manager = Manager.objects.filter(email="manager@example.com").first()

        menu = Menu()
        menu.save()
        restaurant.menu = menu

        restaurant.save()