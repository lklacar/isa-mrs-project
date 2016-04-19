from seeding.seeds.admin_seed import AdminSeed
from seeding.seeds.drink_seed import DrinkSeed
from seeding.seeds.employee_seed import WaiterSeed
from seeding.seeds.food_seed import FoodSeed
from seeding.seeds.guest_seed import GuestSeed
from seeding.seeds.manager_seed import ManagerSeed
from seeding.seeds.restaurant_category_seed import RestaurantCategorySeed
from seeding.seeds.restaurant_seed import RestaurantSeed
from seeding.seeds.system_manager_seed import SystemManagerSeed

SEEDS = [
    ManagerSeed,
    RestaurantCategorySeed,
    AdminSeed,
    GuestSeed,
    RestaurantSeed,
    SystemManagerSeed,
    WaiterSeed,
    FoodSeed,
    DrinkSeed,
]
