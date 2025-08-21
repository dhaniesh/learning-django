from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee
# Create your views here.

def employeeView(request):
    data = Employee.objects.all()
    return JsonResponse({'employees': list(data.values())})