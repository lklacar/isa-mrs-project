from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.login_form import LoginForm
from authentication.forms.register_form import RegisterForm


class LoginView(TemplateView):
    template_name = "authentication/login-or-register.html"

    def get(self, request, *args, **kwargs):
        return redirect("auth:login-or-register")

    def post(self, request):

        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if not user.is_confirmed:
                return HttpResponse("You must confirm your email first.")

            login(request, user)
            if user:
                return redirect("index")

        data = dict(login_form=form, register_form=RegisterForm())

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))
