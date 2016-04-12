from django.conf.urls import url

from system_manager.views import AddRestaurantView

import system_manager.views

urlpatterns = [
    url(r"^add-restaurant/", AddRestaurantView.as_view(), name="add-restaurant"),
    url(r"^home/", system_manager.views.home_view, name="home"),
]
