from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def table_view(request):
    if request.method == "GET":
        return render(request, "manager/tables.html")
    else:
        pass


def add_table_view(request):
    return JsonResponse()
