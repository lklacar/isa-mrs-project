from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from system_manager.forms import AddRestaurantForm
from restaurant.models import Restaurant
from manager.models import Manager


from os import urandom
from django.contrib.sites.shortcuts import get_current_site

class AddRestaurantView(TemplateView):
    template_name = 'system_manager/add-restaurant.html'

    def get(self, request, *args, **kwargs):
        form = AddRestaurantForm()
        data = dict(form=form)
        return render(request, self.template_name, data)

    def post(self, request):
        form = AddRestaurantForm(request.POST)
        data = dict(form=form)
        if form.is_valid():
            data = form.cleaned_data

            restaurant = Restaurant()
            manager = Manager()

            restaurant.email = data['name']
            restaurant.first_name = data['description']
            manager.email = data['manager_email']
            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
            manager.password = "".join([chars[ord(c) % len(chars)] for c in urandom(8)])
            manager.save()

            manager.send_email("Login details - Restaurant booking online",
                               "Your login details :\n E-mail : " + manager.email +
                               "\n Password : " + manager.password + "\n You can login now " +
                               get_current_site(request).domain + "\n Restaurant booking online")


            restaurant.manager = manager
            restaurant.save()

        return render(request, self.template_name, data)
