from django.conf.urls import url

from authentication.views import login_view, register_view, logout_view, login_or_register_view, confirmation_view

urlpatterns = [
    url(r"^$", login_or_register_view.LoginOrRegisterView.as_view(), name="login-or-register"),

    url(r'^login/', login_view.LoginView.as_view(), name="login"),
    url(r'^register/', register_view.RegisterView.as_view(), name="register"),
    url(r'^logout/', logout_view.logout, name="logout"),
    url(r'^confirm/', confirmation_view.confirm, name="confirm"),

]
