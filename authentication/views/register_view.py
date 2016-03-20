from django.contrib.auth.models import Group
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.register_form import RegisterForm
from authentication.models import User


class RegisterView(TemplateView):
    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        data = {'form': RegisterForm()}
        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

    def post(self, request):
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            user = User()
            user.email = data['email']
            user.set_password(data['password1'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()

            group = Group.objects.get(name='Users')
            user.groups.add(group)

            user.save()

            return redirect("index")

        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))
