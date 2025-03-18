from django.urls import path
from users import views

app_name = "users"

urlpatterns = [
    path('login/employee/', views.EmployeeLoginView.as_view(), name='employee_login'),
    path('login/manager/', views.ManagerLoginView.as_view(), name='manager_login'),
    path('login/management/', views.ManagementLoginView.as_view(), name='management_login'),
    path('role_login/', views.role_based_redirect, name='role_redirect'),

    path('login', views.login_dashboard,name='login_dashboard'),
    path('employee', views.employee_dashboard,name='employee_dashboard'),
    path('manager', views.manager_dashboard,name='manager_dashboard'),
    path('management', views.management_dashboard,name='management_dashboard'),
]




