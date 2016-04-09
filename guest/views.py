from django.http import Http404
from django.shortcuts import render

# Create your views here.

from authentication.models import User
from restaurant.models import Restaurant


def profile(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        raise Http404

    return render(request, "guest/profile.html", dict(user=user))


def home(request):
    return render(request, "guest/home.html", dict(restaurants=Restaurant.objects.all()))
