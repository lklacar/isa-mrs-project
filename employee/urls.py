from django.conf.urls import url
from employee.employee_views import IndexView, EditEmployeeView


urlpatterns = [
    url(r"^index/", IndexView.as_view(), name="index"),
    url(r"^edit-profile/", EditEmployeeView.as_view(), name="edit-profile"),
]
