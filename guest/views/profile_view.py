from django.http import Http404
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from guest.models import Guest


class ProfileView(TemplateView):
    template_name = "guest/profile.html"

    def get(self, request, id, *args, **kwargs):
        try:
            user = Guest.objects.filter(id=id).first()
        except:
            raise Http404

        return render(request, self.template_name, dict(user=user))
