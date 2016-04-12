from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from employee.models import Waiter

class HomeView(TemplateView):
    template_name = "employee/waiter/home.html"

    def get(self, request, *args, **kwargs):
        user = Waiter.objects.get(id=request.user.id)
        if user.password_change_count == 0:
            return redirect("employee:index")

        return render(request, self.template_name)