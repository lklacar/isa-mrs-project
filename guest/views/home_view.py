from django.shortcuts import render
from django.views.generic import TemplateView

from restaurant.models import Restaurant


class HomeView(TemplateView):
    template_name = "guest/home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, dict(restaurants=Restaurant.objects.all()))
