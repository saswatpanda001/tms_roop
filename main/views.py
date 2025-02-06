from django.shortcuts import render
from django.contrib.auth import get_user_model
from users.models import UserProfileModel
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "landing.html")

def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def emp_profile(request,pk):
    loggedin_user = request.user
    user_data = UserProfileModel.objects.get(user=loggedin_user)
    skills_data = user_data.skills.all()
    cert_data = user_data.certifications.all()
    training_data = user_data.trainings.all()
    achievements_data = user_data.achievements.all()
    print(achievements_data)
    
   
    data = {"user_data":user_data,"skills":skills_data,"cert_data":cert_data, "achievements_data": achievements_data}
    return render(request, 'profile.html',data)


@login_required
def emp_details(request,pk):

    loggedin_user = request.user
    user_data = UserProfileModel.objects.get(user=loggedin_user)
    data = {"user_data":user_data}


    return render(request, 'profile.html',data)

@login_required
def emp_list(request):
    emp_list = UserProfileModel.objects.all()
    data = {"emp_list":emp_list}
    return render(request, 'emp_list.html', data)

@login_required
def emp_edit(request,pk):
    return render(request, 'emp_edit.html')

@login_required
def emp_skillgap(request,pk):
    return render(request, 'skillgap.html')

@login_required
def emp_training(request,pk):
    return render(request, 'training.html')


@login_required
def feedback(request):
    return render(request, 'feedback.html')


@login_required
def analytics(request):
    return render(request, 'analytics.html')



@login_required
def post(request):
    return render(request, 'post.html')


@login_required
def succession(request):
    return render(request, 'succession.html')



@login_required
def promotion(request):
    return render(request, 'promotion.html')

@login_required
def reports(request):
    return render(request, 'reports.html')



