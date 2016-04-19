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
        form = AddRestaurantForm(request.POST, request.FILES)
        data = dict(form=form)
        if form.is_valid():
            data = form.cleaned_data

            restaurant = Restaurant()
            manager = Manager()

            restaurant.name = data['name']
            restaurant.description = data['description']
            restaurant.profile_image = request.FILES['profile_image']

            manager.email = data['manager_email']
            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

            password = "".join([chars[ord(c) % len(chars)] for c in urandom(8)])
            manager.set_password(password)
            manager.is_confirmed = True
            manager.save()

            manager.send_email("Login details - Restaurant booking online",
                               "Your login details :\n E-mail : " + manager.email +
                               "\n Password : " + password + "\n You can login now " +
                               get_current_site(request).domain + "\n Restaurant booking online")

            restaurant.manager = manager
            restaurant.category = data['category']

            restaurant.save()

        return render(request, self.template_name, dict(form=form))


def home_view(request):
    return render(request, "system_manager/home.html")
