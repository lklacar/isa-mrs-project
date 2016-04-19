import random

from manager.models import Manager
from restaurant.models import Restaurant, Menu, RestaurantCategory
from seeding.seeds.abstract_seed import AbstractSeed


class RestaurantSeed(AbstractSeed):
    def seed(self):
        restaurant_names = [
            'El Celler de Can Roca',
            'Osteria Francescana',
            'Noma',
            'Central',
            'Eleven Madison Park',
            'Mugaritz',
            'Dinner by Heston Blumenthal',
            'Narisawa',
            'D.O.M.',
            'Gaggan',
        ]
        description = """Lorem ipsum dolor sit amet, et mea legere blandit abhorreant, nam exerci accusam elaboraret no. Mea te minimum sensibus. Cu qui commodo omnesque percipit. Per munere nullam temporibus ea. Nec mentitum antiopam no. Ad duis doming indoctum his. Eos ex fabulas singulis, natum labores periculis mea ex.
                        Quo libris apeirian eu. Per solet aperiri ea. Eligendi hendrerit nam id, eos eu alienum antiopam intellegebat, eam viderer denique cu. Homero equidem eu pro.
                        Mel nostro constituam ad, ius ut modus cetero verear. Ad nam eros omnis, mea ei offendit molestiae. Vix adhuc possit inciderint ad, forensibus posidonium sed in, in mei decore vivendo volumus. No per labore nemore. Eos ei molestie percipit maiestatis, oratio audire molestiae ne est, dolore assentior prodesset sed ei.
                        Ea tibique fastidii quo, sit accusata reformidans ei. Elitr primis an quo, quem contentiones eu pro. Eius cotidieque reformidans ex est, rebum expetenda has at. Ius nulla inermis disputando an, idque meliore sit et.
                        Agam reque pericula ne mea, pro postea graeco debitis ne, mei habemus gubergren cotidieque id. Timeam eleifend cu sed, vero labitur per in. Vim ei laoreet minimum officiis, pri alterum gloriatur eu. Id erat debitis comprehensam vix, vix ea dicit dissentiet, cu vix ipsum luptatum. Ad eros ridens malorum eam.""".strip()

        for i in range(len(restaurant_names)):
            restaurant_name = restaurant_names[i]

            restaurant = Restaurant()
            restaurant.name = restaurant_name
            restaurant.description = description
            restaurant.manager = Manager.objects.filter(email="manager%s@example.com" % str(i)).first()
            restaurant.category = random.choice(RestaurantCategory.objects.all())

            menu = Menu()
            menu.save()
            restaurant.menu = menu

            restaurant.save()
