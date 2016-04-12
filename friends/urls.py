from django.conf.urls import url

import friends.views
from utils.url import basic_url

urlpatterns = [
    url(r'^search/', friends.views.search_friends, name="search"),
    url(basic_url("add/{id}"), friends.views.add_friend, name="add"),
    url(basic_url("remove/{id}"), friends.views.remove_friend, name="remove"),
    url(r'^list/', friends.views.list_friends, name="list"),
]
