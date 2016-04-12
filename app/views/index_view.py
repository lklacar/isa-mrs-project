from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

HOMEPAGES = {
    "GUEST": "guest:home",
    "MANAGER": "manager:home",
    "SYSTEM_MANAGER": "system_manager:home",
}


class IndexView(TemplateView):
    @method_decorator(login_required(login_url="auth:login-or-register"))
    def get(self, request, *args, **kwargs):
        role = request.user.role

        return redirect(HOMEPAGES[role])
