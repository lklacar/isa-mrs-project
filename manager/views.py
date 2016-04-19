from os import urandom

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from employee.models import Employee
from manager.forms import AddEmployeeForm, AddFoodForm
from restaurant.models import Restaurant








