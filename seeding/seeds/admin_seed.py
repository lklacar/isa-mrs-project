from authentication.models import User
from seeding.seeds.abstract_seed import AbstractSeed


class AdminSeed(AbstractSeed):
    def seed(self):
        user = User()
        user.email = "l.klacar@vegaitsourcing.rs"
        user.set_password("qweqwe1*")
        user.first_name = "Luka"
        user.last_name = "Klacar"
        user.is_staff = True
        user.is_superuser = True
        user.save()
