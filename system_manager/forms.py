from django import forms
from django.forms import ModelForm

from restaurant.models import Restaurant


class AddRestaurantForm(ModelForm):
    manager_email = forms.EmailField(max_length=254)

    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'profile_image', 'category']



