from django.urls import path
from employees import views

app_name = 'employees'

urlpatterns = [
    path('employees/', views.EmployeeListView.as_view(), name='list'),
    path('add-employee/', views.EmployeeCreateView.as_view(), name='create'),
]
