from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from manager.views.add_drink_view import AddDrinkView
from manager.views.add_employee_view import AddEmployeeView
from manager.views.add_food_view import AddFoodView
from manager.views.home_view import home_view
from manager.views.table_view import table_view

urlpatterns = [
    url(r"^add-employee/", AddEmployeeView.as_view(), name="add-employee"),
    url(r"^add-food/", AddFoodView.as_view(), name="add-food"),
    url(r"^add-drink/", AddDrinkView.as_view(), name="add-drink"),
    url(r"^home/", home_view, name="home"),
    url(r"^tables/", table_view, name="tables"),
]
