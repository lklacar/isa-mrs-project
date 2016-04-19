from restaurant.models import RestaurantCategory
from seeding.seeds.abstract_seed import AbstractSeed


class RestaurantCategorySeed(AbstractSeed):

    def seed(self):
        category_names = [
            'Fast Casual',
            'Family Style',
            'Fine Dining',
            'Cafe or Bistro',
            'Fast Food',
        ]

        for category_name in category_names:
            category = RestaurantCategory(name=category_name)
            category.save()
