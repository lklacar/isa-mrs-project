from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from friendship.models import Friend

from authentication.models import User


def list_friends(request):
    return render(request, "guest/friends.html", dict(friends=Friend.objects.friends(request.user)))


def search_friends(request):
    if request.method == "GET":
        return render(request, "friends/search.html")

    if request.method == "POST":
        users = User.objects.filter(
            Q(first_name__icontains=request.POST['query']) | Q(last_name__icontains=request.POST['query']))

        return render(request, "friends/search.html", dict(users=users))


def add_friend(request, id):
    if request.method == "POST":
        from_user = request.user
        to_user = User.objects.filter(id=id).first()

        friendship = Friend.objects.add_friend(from_user, to_user)
        friendship.accept()

    return redirect("friends:list")

    raise Http404


def remove_friend(request, id):
    if request.method == "POST":
        from_user = request.user
        to_user = User.objects.filter(id=id).first()

        Friend.objects.remove_friend(from_user, to_user)

        return redirect("friends:list")

    raise Http404
