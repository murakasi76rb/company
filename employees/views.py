from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from employees.models import Employee
from employees.forms import EmployeeForm

# Create your views here.

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employees/add_employee.html'
    success_url = reverse_lazy('employees:list')



class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/info-employee.html'
    context_object_name = 'employee'
