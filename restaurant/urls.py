from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from manager.views.add_employee_view import AddEmployeeView
from manager.views.add_food_view import AddFoodView
from manager.views.home_view import home_view
from manager.views.table_view import table_view
from utils.url import basic_url
from restaurant.views import profile_view

urlpatterns = [
    url(basic_url("profile/{id}"), profile_view, name="profile"),

]
