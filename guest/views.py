from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from authentication.models import User



def profile(request, id):
    try:
        user = User.objects.get(id=id)
    except:
        raise Http404

    return render(request, "guest/profile.html", dict(user=user))
