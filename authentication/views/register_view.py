from datetime import datetime, timedelta

from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.login_form import LoginForm
from authentication.forms.register_form import RegisterForm
from authentication.models import User
from authentication.models.confirmation_token import ConfirmationToken
from utils.id import generate_unique_token
from django.contrib.sites.shortcuts import get_current_site


class RegisterView(TemplateView):
    template_name = "authentication/login-or-register.html"

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

            confirmation_token = ConfirmationToken()
            confirmation_token.user = user
            confirmation_token.token = generate_unique_token()
            confirmation_token.expires = datetime.now() + timedelta(days=1)
            confirmation_token.save()

            user.send_email("Confirm your email",
                            "http://" + get_current_site(
                                    request).domain + "/auth/confirm/?token=" + confirmation_token.token)

            """
            group = Group.objects.get(name='Users')
            user.groups.add(group)
            user.save()
            """
            """
            new_user = authenticate(username=data['email'], password=data['password1'])
            login(request, new_user)
            """
            return redirect("index")

        data = dict(login_form=LoginForm(), register_form=form)

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))
