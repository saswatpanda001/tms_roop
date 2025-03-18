from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import get_user_model
from users.models import UserProfileModel, CommonFeedback, DepartmentModel,EnrollmentModel, PositionModel, SkillModel, CertificationModel, AchievementModel, TrainingProgramModel, JobModel, JobApplicationModel
from django.contrib.auth.decorators import login_required
from users.models import BlogModel
from main.forms import BlogForm, FeedbackForm, JobApplicationForm, JobForm, CommonFeedbackForm, UserProfileForm, CommonUserProfileForm
from django.utils import timezone
from django.shortcuts import render, redirect
from main.models import FeedbackModel
from django.contrib import messages
from main.forms import TrainingProgramForm  # The form that you will create below


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    return render(request, "landing.html")


def dashboard(request):
   
    top_user = UserProfileModel.objects.order_by("-avg_score").first()
    enrollments = EnrollmentModel.objects.order_by("-enrollment_date")[:3]
    users = UserProfileModel.objects.all()

    total_emp = len(users)

    feedback = FeedbackModel.objects.all()
    avg_rating = 0
    for each in feedback:
        if(each.rating):
            avg_rating+=int(each.rating)
    if len(feedback)>0:
        avg_rating/=len(feedback)
    
    data = {"avg_rating":avg_rating,"total_emp":total_emp,"top_user":top_user,"enrollments":enrollments}

    return render(request, "dashboard.html",data)


@login_required
def emp_profile(request,pk):
    loggedin_user = request.user
    user_data = UserProfileModel.objects.get(user=loggedin_user)
    skills_data = user_data.skills.all()
    skill_gap = user_data.skill_gap.all()
    cert_data = user_data.certifications.all()
    training_data = user_data.trainings.all()
    achievements_data = user_data.achievements.all()


    data = {"training_data":training_data,"user_data":user_data,"skill_gap":skill_gap,"skills":skills_data,"cert_data":cert_data, "achievements_data": achievements_data}
    return render(request, 'profile.html',data)

def edit_profile(request,pk):
    # Get the current user's profile (assuming UserProfileModel has a OneToOne relation with User)
    user_profile = UserProfileModel.objects.get(user__id=pk)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        # Check if form is valid and save it
        if form.is_valid():
            form.save()  # This will automatically handle saving many-to-many relationships
            if pk==request.user.id:
                return redirect('main:emp_profile', pk)
            else:
                return redirect('main:emp_list')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile_edit.html', {'form': form})


@login_required
def emp_details(request, pk):
    user_data = get_object_or_404(UserProfileModel, user__id=pk)
    
    context = {
        "user_data": user_data,
        "skills": user_data.skills.all(),
        "skill_gap": user_data.skill_gap.all(),
        "cert_data": user_data.certifications.all(),
        "achievements_data": user_data.achievements.all(),
        "training_data":user_data.trainings.all()
    }

    return render(request, 'emp_details.html', context)

@login_required
def emp_list(request):
    emp_list = UserProfileModel.objects.filter(role="employee")
    position = PositionModel.objects.all()
    data = {"emp_list":emp_list,"position":position}
    return render(request, 'emp_list.html', data)

@login_required
def emp_edit(request,pk):
    return render(request, 'emp_edit.html')

@login_required
def emp_skillgap(request,pk):
    user_profile = UserProfileModel.objects.get(user__id=pk)
    # Get the user's skill gap
    skill_gap = user_profile.skill_gap.all()

    # Find training programs that cover the missing skills
    training_programs = TrainingProgramModel.objects.filter(skills__in=skill_gap).distinct()

    context = {
        "skill_gap": skill_gap,
        "training_programs": training_programs
    }

    return render(request, "skillgap.html", context)


@login_required
def training_programs_view(request):
    """Display a list of all available training programs."""
    training_programs = TrainingProgramModel.objects.all()
    context = {"training_programs": training_programs}
    return render(request, 'training.html', context)



@login_required
def program_detail(request, program_id):
    program = get_object_or_404(TrainingProgramModel, id=program_id)
    user_profile = UserProfileModel.objects.get(user=request.user)
    
    # Check if the user is already enrolled
    is_enrolled = EnrollmentModel.objects.filter(user=request.user, program=program).exists()
    enrolled_users = EnrollmentModel.objects.filter(program=program).select_related('user')

    return render(request, 'program_detail.html', {
        'program': program,
        'is_enrolled': is_enrolled,
        'enrolled_users': enrolled_users
    })

@login_required
def enroll_in_program(request, program_id):
    program = get_object_or_404(TrainingProgramModel, id=program_id)
    user_profile = UserProfileModel.objects.get(user=request.user)

    # Check if user is already enrolled
    if not EnrollmentModel.objects.filter(user=request.user, program=program).exists():
        # Add enrollment entry
        EnrollmentModel.objects.create(user=request.user, program=program)

        # Add skills to user profile
        user_profile.skills.add(*program.skills.all())

        # Remove these skills from user's skill gap
        user_profile.skill_gap.remove(*program.skills.all())

        # Add training to user's profile
        user_profile.trainings.add(program)

        user_profile.save()

    return redirect('main:program_detail', program_id=program.id)


def common_edit_profile(request):
    user_profile = UserProfileModel.objects.get(user=request.user)
    if request.method == 'POST':
        form = CommonUserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('main:emp_profile', request.user.id)  # Change to your profile view name
    else:
        form = CommonUserProfileForm(instance=user_profile)
    
    return render(request, 'common_edit_profile.html', {'form': form})



@login_required
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.sender = request.user  # Assigning the logged-in user
            feedback.profile = UserProfileModel.objects.filter(user=request.user)[0]
            feedback.created_on = timezone.now()
            feedback.save()
            return redirect('main:feedback')  # Refresh the page after submission
    else:
        form = FeedbackForm()

    feedbacks = FeedbackModel.objects.all().order_by('-created_on')  # Fetch all feedbacks sorted by latest
    feedback_user = FeedbackModel.objects.filter(receiver=request.user)
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




def add_training_program(request):
    if request.method == 'POST':
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            # Save the new training program
            training_program = form.save()

            # Display success message
            messages.success(request, 'Training program added successfully!')
            return redirect('main:add_training_program')  # Redirect to the same page or another page as required
    else:
        form = TrainingProgramForm()

    return render(request, 'add_training_program.html', {'form': form})

@login_required
def post_job(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        JobModel.objects.create(
            title=title,
            description=description,
            posted_by=request.user
        )

        return redirect("main:job_list")

    return render(request, "HR/post_job.html")

@login_required
def job_list(request):
    jobs = JobModel.objects.all()
    return render(request, "Employee/job_list.html", {"jobs": jobs})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(JobModel, id=pk)
    applications = JobApplicationModel.objects.filter(job=job)  # Fetch applicants for this job

    return render(request, "Employee/job_detail.html", {"job": job, "applications": applications})




@csrf_exempt
def update_application_status(request):
    if request.method == "POST":
        data = json.loads(request.body)
        application_id = data.get("application_id")
        new_status = data.get("status")

        try:
            application = JobApplicationModel.objects.get(id=application_id)
            application.status = new_status
            application.save()
            return JsonResponse({"success": True})
        except JobApplicationModel.DoesNotExist:
            return JsonResponse({"success": False, "error": "Application not found"})

    return JsonResponse({"success": False, "error": "Invalid request"})



@login_required
def apply_job(request, pk):
    job = get_object_or_404(JobModel, id=pk)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect("main:job_list")
    else:
        form = JobApplicationForm()
    return render(request, "Employee/apply_job.html", {"form": form, "job": job})


@login_required
def edit_job(request, pk):
    job = get_object_or_404(JobModel, pk=pk)
    
    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect("main:job_detail", pk=job.pk)
    else:
        form = JobForm(instance=job)

    return render(request, "Manager/edit_job.html", {"form": form, "job": job})



@login_required
def applied_jobs(request):
    applications = JobApplicationModel.objects.filter(applicant=request.user)
    return render(request, "Employee/applied_jobs.html", {"applications": applications})


from django.db.models import Count

@login_required
def talent_view(request):
    profiles = UserProfileModel.objects.annotate(
        total_skills=Count('skills'),
        total_certifications=Count('certifications'),
        total_trainings=Count('trainings')
    ).filter(
        avg_score__gte=400,  # Employees with performance >= 80%
        avg_rating__gte=4,        # Employees with avg rating >= 4
        experience_years__gte=2,  # Employees with at least 2 years of experience
        total_skills__gt=5,       # Skills must be greater than 5
        total_certifications__gt=5,  # Certifications must be greater than 5
        total_trainings__gt=5  # Trainings must be greater than 5
    ).order_by('-avg_score', '-avg_performance')  # Sorting by best scores

    
    return render(request, 'HR/talent.html', {'profiles': profiles})


def skill_gap_analysis(request, user_id):
    user = get_object_or_404(UserProfileModel, id=user_id)
    
    # Find missing skills
    current_skills = set(user.skills.all())
    required_skills = set(user.skill_gap.all())
    missing_skills = required_skills - current_skills

    # Update skill_gap field
    user.skill_gap.set(missing_skills)

    # Find training programs covering missing skills
    recommended_training = TrainingProgramModel.objects.filter(skills__in=missing_skills).distinct()

    # Fetch enrolled programs
    enrolled_programs = user.enrolled_programs.all()

    # Prepare data for the template
    gap_analysis = [{
        "employee": user,
        "missing_skills": missing_skills,
        "recommended_training": recommended_training
    }]

    context = {
        "gap_analysis": gap_analysis,
        "training_programs": recommended_training,
        "enrolled_programs": enrolled_programs
    }
    
    return render(request, "skillgap.html", context)


def enroll_training(request, user_id, training_id):
    user = get_object_or_404(UserProfileModel, id=user_id)
    training = get_object_or_404(TrainingProgramModel, id=training_id)
    
    user.enrolled_programs.add(training)
    return redirect("skill_gap_analysis", user_id=user.id)



@login_required
def commonfeedback_view(request):
    feedbacks = CommonFeedback.objects.filter(sender=request.user).order_by('-created_at')  # Show only user's feedback
    feedbacks_all = CommonFeedback.objects.all().order_by('-created_at')  # Show only user's feedback

    if request.method == "POST":
        form = CommonFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.sender = request.user
            feedback.save()
            return redirect('main:commonfeedback_view')
    else:
        form = CommonFeedbackForm()

    return render(request, 'common_feedback.html', {'form': form, 'feedbacks': feedbacks,'feedbacks_all':feedbacks_all})
