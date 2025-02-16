from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from users.models import UserProfileModel, DepartmentModel, PositionModel, SkillModel, CertificationModel, AchievementModel
from django.contrib.auth.decorators import login_required
from users.models import BlogModel
from main.forms import BlogForm, FeedbackForm  
from django.utils import timezone
from django.shortcuts import render, redirect
from main.models import FeedbackModel

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
def edit_profile(request,pk):
    user_profile = UserProfileModel.objects.get(user__id=pk)

    if request.method == "POST":
        user_profile.user.username = request.POST.get("username", user_profile.user.username)
        user_profile.role = request.POST.get("role", user_profile.role)
        user_profile.phone_number = request.POST.get("phone_number", user_profile.phone_number)
        user_profile.email = request.POST.get("email", user_profile.email)
        user_profile.address = request.POST.get("address", user_profile.address)
        user_profile.experience_years = request.POST.get("experience_years", user_profile.experience_years)
        user_profile.rating = request.POST.get("rating", user_profile.rating)

        if "image" in request.FILES:
            user_profile.image = request.FILES["image"]

        # Update Many-to-Many Fields
        user_profile.skills.set(request.POST.getlist("skills"))
        user_profile.certifications.set(request.POST.getlist("certifications"))
        user_profile.achievements.set(request.POST.getlist("achievements"))

        user_profile.save()
        user_profile.user.save()

        
        return redirect("main:emp_profile", pk=request.user.id)  # Redirect to profile page

    # Pass all available skills, certifications, achievements for selection
    context = {
        "user_data": user_profile,
        "all_skills": SkillModel.objects.all(),
        "all_certifications": CertificationModel.objects.all(),
        "all_achievements": AchievementModel.objects.all(),
    }
    return render(request, "profile_edit.html", context)




@login_required
def emp_details(request,pk):

    loggedin_user = request.user
    user_data = UserProfileModel.objects.get(user=loggedin_user)
    data = {"user_data":user_data}


    return render(request, 'profile.html',data)

@login_required
def emp_list(request):
    emp_list = UserProfileModel.objects.all()
    position = PositionModel.objects.all()
    print(position)
    data = {"emp_list":emp_list,"position":position}
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
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user  # Assigning the logged-in user
            feedback.profile = UserProfileModel.objects.filter(user=request.user)[0]
            feedback.created_on = timezone.now()
            feedback.save()
            return redirect('main:feedback')  # Refresh the page after submission

    else:
        form = FeedbackForm()

    feedbacks = FeedbackModel.objects.all().order_by('-created_on')  # Fetch all feedbacks sorted by latest
    feedback_user = FeedbackModel.objects.filter(user=request.user)
    data = {'form': form, 'feedback_user': feedback_user,'feedback_all':feedbacks}
    return render(request, 'feedback.html', data)


@login_required
def analytics(request):
    return render(request, 'analytics.html')




@login_required
def post_view(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user.userprofilemodel  # Assuming UserProfileModel is linked to User
            blog.publish_date = timezone.now()
            blog.save()
            return redirect('main:posts')  # Refresh the page after submission

    else:
        form = BlogForm()

    posts = BlogModel.objects.all().order_by('-publish_date')  # Fetch all posts sorted by latest
    return render(request, 'post.html', {'form': form, 'posts': posts})



@login_required
def succession(request):
    return render(request, 'succession.html')



@login_required
def promotion(request):
    return render(request, 'promotion.html')

@login_required
def reports(request):
    return render(request, 'reports.html')



