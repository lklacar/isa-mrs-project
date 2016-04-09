from django import forms
from django.forms import ModelForm

from employee.models import Employee
from restaurant.models import Food, Restaurant


class AddEmployeeForm(ModelForm):
    CHOICES = [('waiter', 'Waiter'),
               ('chef', 'Chef'),
               ('bartender', 'Bartender')]

    type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Employee
        fields = ['email', 'first_name', 'last_name', 'shoe_size', 'clothes_size']


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
