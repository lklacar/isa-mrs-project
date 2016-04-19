import random

from restaurant.models import Food, Menu, Drink
from seeding.seeds.abstract_seed import AbstractSeed


class DrinkSeed(AbstractSeed):
    def seed(self):
        drinks_list = """
        Crazy Tempest
        Blueberry Jam
        Palm Enigma
        Salt 'n Pepper Volley
        Cranberry Rum
        Vodka Shield
        Oak Punch
        Apple Whistle
        Sanguine Sour
        Hazelnut Espresso
        Wasabi Snowball
        Mango Petal
        Strawberry Wacker
        Coffee Infusion
        Garlic Earthquake
        Rainbow Snake
        Light Ale Infusion
        Lime Twilight
        Demon Smooch
        Sherry Mud
        Holy Sake
        Incredible Twilight
        Rushed Arrow
        Dire Lady
        Mango Kiss
        Beautiful Vengeance
        Icy Brew
        Rosemary Sherry
        Garlic Volley
        Watermelon Rage
        Lavender Puff
        Light Ale Nightfall
        White Wine Squeeze
        Perfect Hopper
        Summer Wonder
        Paranoid Drink
        Nutty Torrent
        Honest Shot
        Tea Infusion
        Oak Mud
        """.strip().split("\n")

        description = """Lorem ipsum dolor sit amet, et mea legere blandit abhorreant, nam exerci accusam elaboraret no. Mea te minimum sensibus. Cu qui commodo omnesque percipit. Per munere nullam temporibus ea. Nec mentitum antiopam no. Ad duis doming indoctum his. Eos ex fabulas singulis, natum labores periculis mea ex.
            Quo libris apeirian eu. Per solet aperiri ea. Eligendi hendrerit nam id, eos eu alienum antiopam intellegebat, eam viderer denique cu. Homero equidem eu pro.
            Mel nostro constituam ad, ius ut modus cetero verear. Ad nam eros omnis, mea ei offendit molestiae. Vix adhuc possit inciderint ad, forensibus posidonium sed in, in mei decore vivendo volumus. No per labore nemore. Eos ei molestie percipit maiestatis, oratio audire molestiae ne est, dolore assentior prodesset sed ei.
            Ea tibique fastidii quo, sit accusata reformidans ei. Elitr primis an quo, quem contentiones eu pro. Eius cotidieque reformidans ex est, rebum expetenda has at. Ius nulla inermis disputando an, idque meliore sit et.
            Agam reque pericula ne mea, pro postea graeco debitis ne, mei habemus gubergren cotidieque id. Timeam eleifend cu sed, vero labitur per in. Vim ei laoreet minimum officiis, pri alterum gloriatur eu. Id erat debitis comprehensam vix, vix ea dicit dissentiet, cu vix ipsum luptatum. Ad eros ridens malorum eam.""".strip()

        for drink_name in drinks_list:
            food = Drink()
            food.name = drink_name.strip()
            food.description = description
            food.price = random.uniform(100, 1000)
            food.menu = random.choice(Menu.objects.all())
            food.save()
