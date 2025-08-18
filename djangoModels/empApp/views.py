from django.shortcuts import render
from empApp.models import Employee
# Create your views here.


def employee_data(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})
