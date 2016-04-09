from django.shortcuts import redirect, render_to_response, render
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.login_form import LoginForm
from authentication.forms.register_form import RegisterForm


class LoginOrRegisterView(TemplateView):
    template_name = "authentication/login-or-register.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect("index")

        data = dict(login_form=LoginForm(), register_form=RegisterForm())

        return render(request, self.template_name, data)
