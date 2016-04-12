from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from employee.models import Employee
from employee.forms.profile import EditPasswordForm, EditEmployeeForm


class IndexView(TemplateView):
    template_name = "employee/index.html"

    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(id=request.user.id)
        form = EditPasswordForm(instance=user)
        return render(request, self.template_name, dict(user=user, form=form))

    def post(self, request):
        user = Employee.objects.get(id=request.user.id)
        form = EditPasswordForm(request.POST, instance=user)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['confirm_password']:
                user.set_password(data['password'])
                user.password_change_count += 1
                user.save()
                return redirect("app:index")

        return render(request, self.template_name, dict(form=form))


class EditEmployeeView(TemplateView):
    template_name = "employee/edit-profile.html"

    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(id=request.user.id)
        form = EditEmployeeForm(instance=user)
        data = dict(form=form)
        return render(request, self.template_name, data)

    def post(self, request):
        user = Employee.objects.get(id=request.user.id)
        form = EditEmployeeForm(request.POST, instance=user)
        if form.is_valid():
            data = form.cleaned_data

            if user.check_password(data['current_password']):
                if data['password'] == data['confirm_password']:
                    user.email = data['email']
                    user.first_name = data['first_name']
                    user.last_name = data['last_name']
                    user.shoe_size = data['shoe_size']
                    user.clothes_size = data['clothes_size']
                    user.set_password(data['password'])
                    if data['password'] != "":
                        user.password_change_count += 1
                    user.save()
                    return redirect("app:index")

        return render(request, self.template_name, dict(form=form))
