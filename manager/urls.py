from django.conf.urls import url

from manager.views import AddEmployeeView

urlpatterns = [
    url(r"^add-employee/", AddEmployeeView.as_view(), name="add-employee"),

]
