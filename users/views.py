from django.shortcuts import render, redirect, get_list_or_404
from allauth.account.views import LoginView
from django.contrib.auth.decorators import login_required
from users.models import UserProfileModel
from main.forms import JobApplicationForm, JobForm

class EmployeeLoginView(LoginView):
    template_name = "account/login_employee.html"

class ManagerLoginView(LoginView):
    template_name = "account/login_manager.html"

class ManagementLoginView(LoginView):
    template_name = "account/login_management.html"


@login_required
def role_based_redirect(request):
    user = request.user
   
    profile_data = UserProfileModel.objects.filter(user=user)
    if len(profile_data)==0:
        return redirect("users:login")
    else:
        profile_data = profile_data[0]
        if profile_data.role=="employee":
            return redirect('users:employee_dashboard')
        elif profile_data.role=="manager":
            return redirect('users:manager_dashboard')
        elif profile_data.role=="HR":
            return redirect('users:management_dashboard')
        else:
            return redirect('users:login_dashboard')
        
   


def login_dashboard(request):
    return render(request,"login_dashboard.html")
    
def employee_dashboard(request):
    data = UserProfileModel.objects.filter(user=request.user)
    if len(data)==0:
        return redirect("users:employee_login")
    else:
        data = data[0]
        if data.role=="employee":
            return render(request,"employee_dash.html")
        else:
            return redirect("users:employee_login")
            
def manager_dashboard(request):
    data = UserProfileModel.objects.filter(user=request.user)
    if len(data)==0:
        return redirect("users:manager_login")
    else:
        data = data[0]
        if data.role=="manager":
            return render(request,"manager_dash.html")
        else:
            return redirect("users:manager_login")

    

def management_dashboard(request):
    data = UserProfileModel.objects.filter(user=request.user)
    if len(data)==0:
        return redirect("users:management_login")
    else:
        data = data[0]
        if data.role=="HR":
            return render(request,"management_dash.html")
        else:
            return redirect("users:management_login")




