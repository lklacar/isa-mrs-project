from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from manager.forms import AddFoodForm, AddDrinkForm


class AddDrinkView(TemplateView):
    template_name = "manager/add-drink.html"

    def get(self, request, *args, **kwargs):
        form = AddDrinkForm()

        return render(request, self.template_name, dict(form=form))

    def post(self, request):
        form = AddFoodForm(request.POST)
        data = dict(form=form)
        if form.is_valid():
            form.save(request=request, commit=True)

        return render(request, self.template_name, data)
