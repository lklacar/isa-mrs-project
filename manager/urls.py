from django.conf.urls import url

from manager.views import AddEmployeeView, AddFoodView

import manager.views

urlpatterns = [
    url(r"^add-employee/", AddEmployeeView.as_view(), name="add-employee"),
    url(r"^add-food/", AddFoodView.as_view(), name="add-food"),
    url(r"^home/", manager.views.home_view, name="home"),
]
