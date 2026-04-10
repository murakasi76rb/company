from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from employees.models import Employee
from employees.forms import EmployeeForm

# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee.html'


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/add_employee.html'
    success_url = 'employees:list'
