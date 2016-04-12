from django import forms
from django.forms import ModelForm

from employee.models import Employee


class EditEmployeeForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    current_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Employee
        fields = ['email', 'first_name', 'last_name', 'shoe_size', 'clothes_size']


class EditPasswordForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Employee
        fields = []

