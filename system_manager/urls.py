from django.conf.urls import url

from system_manager.views import AddRestaurantView

urlpatterns = [
    url(r"^add-restaurant/", AddRestaurantView.as_view(), name="add-restaurant"),

]
