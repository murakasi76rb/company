from django.urls import path
from employees import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('create/', views.EmployeeCreateView.as_view(), name='create'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('bulk-create/', views.employee_bulk_create_view, name='bulk_create'),
]
