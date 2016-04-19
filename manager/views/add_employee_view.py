from os import urandom

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from employee.models import Employee
from manager.forms import AddEmployeeForm
from restaurant.models import Restaurant


class AddEmployeeView(TemplateView):
    template_name = 'manager/add-employee.html'

    def get(self, request, *args, **kwargs):
        form = AddEmployeeForm()
        data = dict(form=form)

        return render(request, self.template_name, data)

    def post(self, request):
        form = AddEmployeeForm(request.POST)
        data = dict(form=form)
        if form.is_valid():
            data = form.cleaned_data

            employee = Employee()
            employee.email = data['email']
            employee.first_name = data['first_name']
            employee.last_name = data['last_name']
            employee.shoe_size = data['shoe_size']
            employee.clothes_size = data['clothes_size']
            employee.role = data['role']

            chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"

            password = "".join([chars[ord(c) % len(chars)] for c in urandom(8)])
            employee.set_password(password)
            employee.is_confirmed = True

            restaurant = Restaurant.objects.filter(manager=request.user)[0]

            employee.works_in = restaurant

            employee.save()

            employee.send_email("Login details - Restaurant booking online",
                                "Your login details :\n E-mail : " + employee.email +
                                "\n Password : " + password + "\n You can login now " +
                                get_current_site(request).domain + "\n Restaurant booking online")

            employee.save()

        return render(request, self.template_name, dict(form=form))
