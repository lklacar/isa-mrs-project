from django.conf.urls import url


from guest.views.home_view import HomeView
from guest.views.profile_view import ProfileView
from utils.url import basic_url

urlpatterns = [
    url(basic_url("profile/{id}"), ProfileView.as_view(), name="profile"),
    url(r'^home/', HomeView.as_view(), name="home"),

]
