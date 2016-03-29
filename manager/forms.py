from django import forms
from django.forms import ModelForm

from employee.models import Employee


class AddEmployeeForm(ModelForm):
    CHOICES = [('waiter', 'Waiter'),
               ('chef', 'Chef'),
               ('bartender', 'Bartender')]

    type = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Employee
        fields = ['email', 'first_name', 'last_name', 'shoe_size', 'clothes_size']


