from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.login_form import LoginForm
from authentication.forms.register_form import RegisterForm
from authentication.models import User


class RegisterView(TemplateView):
    template_name = "authentication/login-or-register.html.html"

    def get(self, request, *args, **kwargs):
        return redirect("auth:login-or-register")

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User()
            user.email = data['email']
            user.set_password(data['password1'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            """
            group = Group.objects.get(name='Users')
            user.groups.add(group)
            user.save()
            """

            new_user = authenticate(username=data['email'], password=data['password1'])
            login(request, new_user)

            return redirect("index")

        data = dict(login_form=LoginForm(), register_form=form)

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))
