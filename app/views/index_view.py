from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from employee.models import Employee
from guest.models import Guest
from manager.models import Manager
from system_manager.models import SystemManager

HOMEPAGES = {
    Guest: "guest:home",
    Manager: "manager:home",
    SystemManager: "system_manager:home",
}


class IndexView(TemplateView):
    @method_decorator(login_required(login_url="auth:login-or-register"))
    def get(self, request, *args, **kwargs):

        user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user

        for UserType in HOMEPAGES:
            if type(user) == UserType:
                return redirect(HOMEPAGES[UserType])

        if type(user) == Employee:
            return redirect("employee:index")
