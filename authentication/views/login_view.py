from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from authentication.forms.login_form import LoginForm
from django.shortcuts import redirect


class LoginView(TemplateView):
    template_name = "authentication/login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect("index")

        data = {'form': LoginForm()}

        if 'next' in data.keys():
            data['next'] = request.GET['next']

        return render_to_response(self.template_name, data, context_instance=RequestContext(request))

    def post(self, request):

        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            login(request, user)
            if user:
                if form.data['next'] != "":
                    return HttpResponseRedirect(form.data['next'])
                else:
                    return redirect("index")




        return render_to_response(self.template_name, {'form': form}, context_instance=RequestContext(request))
