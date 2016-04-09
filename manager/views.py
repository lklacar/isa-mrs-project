from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from employee.models import Waiter, Chef, Bartender
from manager.forms import AddEmployeeForm, AddFoodForm
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

            if data['type'] == 'waiter':
                employee = Waiter()
            elif data['type'] == 'chef':
                employee = Chef()
            elif data['type'] == 'bartender':
                employee = Bartender()
            else:
                return HttpResponseBadRequest("Employee type does not exists")

            employee.email = data['email']
            employee.first_name = data['first_name']
            employee.last_name = data['last_name']
            employee.shoe_size = data['shoe_size']
            employee.clothes_size = data['clothes_size']

            restaurant = Restaurant.objects.filter(manager=request.user)[0]

            employee.works_in = restaurant
            employee.save()

        return render(request, self.template_name, data)


class AddFoodView(TemplateView):
    template_name = "manager/add-food.html"

    def get(self, request, *args, **kwargs):
        form = AddFoodForm()

        return render(request, self.template_name, dict(form=form))

    def post(self, request):
        form = AddFoodForm(request.POST)
        data = dict(form=form)
        if form.is_valid():
            form.save(request=request, commit=True)

        return render(request, self.template_name, data)
