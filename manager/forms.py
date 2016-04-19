from django import forms
from django.forms import ModelForm

from employee.models import Employee
from restaurant.models import Food, Restaurant, Drink


class AddEmployeeForm(ModelForm):
    CHOICES = [('waiter', 'Waiter'),
               ('chef', 'Chef'),
               ('bartender', 'Bartender')]

    class Meta:
        model = Employee
        fields = ['email', 'first_name', 'last_name', 'shoe_size', 'clothes_size', "role"]


class AddFoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ('name', 'description', 'price')

    # noinspection PyMethodOverriding
    def save(self, request, commit=True):
        data = self.cleaned_data
        food = Food()
        food.name = data['name']
        food.description = data['description']
        food.price = data['price']
        food.menu = Restaurant.objects.filter(manager=request.user).first().menu
        food.save()


class AddDrinkForm(ModelForm):
    class Meta:
        model = Drink
        fields = ('name', 'description', 'price')

    # noinspection PyMethodOverriding
    def save(self, request, commit=True):
        data = self.cleaned_data
        drink = Drink()
        drink.name = data['name']
        drink.description = data['description']
        drink.price = data['price']
        drink.menu = Restaurant.objects.filter(manager=request.user).first().menu
        drink.save()
