"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

import app.views
from app.views.index_view import IndexView

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include("authentication.urls", namespace='auth'), name="auth"),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^guest/', include('guest.urls', namespace='guest'), name='guest'),
    url(r'^manager/', include('manager.urls', namespace='manager'), name='manager'),
    url(r'^system_manager/', include('system_manager.urls', namespace='system_manager'), name='system_manager'),
    url(r'^friends/', include('friends.urls', namespace='friends'), name='friends'),
    url(r'^waiter/', include('employee.waiter_urls', namespace='waiter'), name='waiter'),
    url(r'^employee/', include('employee.urls', namespace='employee'), name='employee'),
    url(r'^restaurant/', include('restaurant.urls', namespace='restaurant'), name='restaurant'),
]
