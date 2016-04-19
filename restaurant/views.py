from django.shortcuts import render

from restaurant.models import Restaurant, Menu, Food, Drink


def profile_view(request, id):
    restaurant = Restaurant.objects.filter(id=id).first()
    food = Food.objects.filter(menu=Menu.objects.filter(restaurant=restaurant))
    drinks = Drink.objects.filter(menu=Menu.objects.filter(restaurant=restaurant))

    data = dict(restaurant=restaurant, food=food, drinks=drinks)

    return render(request, "restaurant/profile.html", data)
