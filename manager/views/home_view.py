from django.shortcuts import render

# Create your views here.

from restaurant.models import Restaurant, Food, Drink, Menu


def home_view(request):
    user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
    restaurant = Restaurant.objects.filter(manager=user).first()
    food = Food.objects.filter(menu=Menu.objects.filter(restaurant=restaurant))
    drinks = Drink.objects.filter(menu=Menu.objects.filter(restaurant=restaurant))

    data = dict(restaurant=restaurant, food=food, drinks=drinks)

    return render(request, "manager/home.html", data)
