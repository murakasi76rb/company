from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.list import ListView
from employees.models import Employee
from employees.forms import EmployeeForm

# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee.html'
    