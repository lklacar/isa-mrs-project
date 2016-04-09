from django.conf.urls import url

import guest.views
from utils.url import basic_url

urlpatterns = [
    url(basic_url("profile/{id}"), guest.views.profile, name="profile"),
    url(r'^home/', guest.views.home, name="home"),

]
