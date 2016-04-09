from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "app/index.html"

    @method_decorator(login_required(login_url="auth:login-or-register"))
    def get(self, request, *args, **kwargs):
        role = request.user.role()

        if role == "guest":
            return redirect("guest:home")
        
        return render(request, self.template_name)
