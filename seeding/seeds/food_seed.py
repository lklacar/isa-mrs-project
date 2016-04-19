import random

from restaurant.models import Food, Menu
from seeding.seeds.abstract_seed import AbstractSeed


class FoodSeed(AbstractSeed):
    def seed(self):
        food_list = """
        Gentle-Fried Mint & Orange Turkey
        Stewed Fennel & Garlic Mutton
        Stewed Hazelnut Crocodile
        Deep-Fried Potatoes & Lobster
        Seared Mustard & Thyme Gratin
        Dried Nuts & Taco
        Nutmeg and Chocolate Custard
        Licorice and Ginger Tarte Tatin
        Mango Snacks
        White Chocolate Cobbler
        Pickled Vanilla Mammoth
        Tenderized Nuts & Bear
        Smoked Parsnip & Pear Tuna
        Pressure-Fried Chilli Crab
        Deep-Fried Parmesan Kebabs
        Infused White Wine Winter Greens
        Licorice and Avocado Jelly
        Date and Passion Fruit Trifle
        Papaya Pie
        Cocoa Crispies
        Basted Ginger & Honey Pigeon
        Shallow-Fried Saffron Chicken
        Deep-Fried Dark Beer Alligator
        Pressure-Cooked Honey-Coated Herring
        Deep-Fried Carrot & Violet Spring Vegetables
        Cured Walnuts & Omelette
        Mint and Raspberry Tart
        Gooseberry and Walnut Sundae
        Cocoa Toast
        Coffee Pie
        Get food names
        Gentle-Fried Lime-Coated Horse
        Thermal-Cooked Sweet & Savory Mutton
        Pan-Fried Honey & Almond Alligator
        Basted Chilli Herring
        Tenderized Curry of Bruschetta
        Pressure-Fried Black Pepper Lasagne
        Banana and Chocolate Whip
        Honey and Chestnut Genoise
        Pistachio Toast
        Lemon Strudel
        """.strip().split("\n")

        description = """Lorem ipsum dolor sit amet, et mea legere blandit abhorreant, nam exerci accusam elaboraret no. Mea te minimum sensibus. Cu qui commodo omnesque percipit. Per munere nullam temporibus ea. Nec mentitum antiopam no. Ad duis doming indoctum his. Eos ex fabulas singulis, natum labores periculis mea ex.
            Quo libris apeirian eu. Per solet aperiri ea. Eligendi hendrerit nam id, eos eu alienum antiopam intellegebat, eam viderer denique cu. Homero equidem eu pro.
            Mel nostro constituam ad, ius ut modus cetero verear. Ad nam eros omnis, mea ei offendit molestiae. Vix adhuc possit inciderint ad, forensibus posidonium sed in, in mei decore vivendo volumus. No per labore nemore. Eos ei molestie percipit maiestatis, oratio audire molestiae ne est, dolore assentior prodesset sed ei.
            Ea tibique fastidii quo, sit accusata reformidans ei. Elitr primis an quo, quem contentiones eu pro. Eius cotidieque reformidans ex est, rebum expetenda has at. Ius nulla inermis disputando an, idque meliore sit et.
            Agam reque pericula ne mea, pro postea graeco debitis ne, mei habemus gubergren cotidieque id. Timeam eleifend cu sed, vero labitur per in. Vim ei laoreet minimum officiis, pri alterum gloriatur eu. Id erat debitis comprehensam vix, vix ea dicit dissentiet, cu vix ipsum luptatum. Ad eros ridens malorum eam.""".strip()

        for food_name in food_list:
            food = Food()
            food.name = food_name.strip()
            food.description = description
            food.price = random.uniform(100, 1000)
            food.menu = random.choice(Menu.objects.all())
            food.save()
