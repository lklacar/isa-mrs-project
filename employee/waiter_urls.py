from django.conf.urls import url
from employee.views.home_view import HomeView

urlpatterns = [
    url(r'^home/', HomeView.as_view(), name="home"),

]
