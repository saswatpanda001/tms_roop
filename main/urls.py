
from django.urls import path
from main import views;


app_name = "main"

urlpatterns = [
    path('', views.home, name="landing_page"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('emp/profile/<int:pk>', views.emp_profile, name="emp_profile"),
    path('emp/profile/edit/<int:pk>', views.edit_profile, name="profile_edit"),
    path('emp/details/<int:pk>', views.emp_details, name="emp_details"),   
    path('emp/list', views.emp_list, name="emp_list"),
    path('emp/edit/<int:pk>', views.emp_edit, name="emp_edit"),
    path('emp/skillgap/<int:pk>', views.emp_skillgap, name="emp_skillgap"),
    
    path('feedback', views.feedback, name="feedback"),

    path('emp/analytics', views.analytics, name="analytics"),
    path('posts', views.post_view, name="posts"),
    path('emp/succession', views.succession, name="succession"),
    path('emp/promotion', views.promotion, name="promotion"),
    path('emp/reports', views.reports, name="reports"),
    path('add-training/', views.add_training_program, name='add_training_program'),

    path('trainings/', views.training_programs_view, name='emp_training'),
    path('trainings/enroll/<int:program_id>/', views.enroll_training, name='enroll_training'),

    path('jobs', views.job_list, name='job_list'),  # View all jobs
    path('jobs/post/', views.post_job, name='post_job'),  # Post a job
    path('jobs/<int:pk>/', views.job_detail, name='job_detail'),  # View a job
    path('jobs/<int:pk>/edit/', views.edit_job, name='edit_job'),  # Edit a job
    path('jobs/<int:pk>/apply/', views.apply_job , name='apply_job'),
    path("my-applied-jobs/", views.applied_jobs, name="applied_jobs"),
    path("update_application_status/", views.update_application_status, name="update_application_status"),

    path('talent/', views.talent_view, name='talent'),
    path('commonfeedback/', views.commonfeedback_view, name='commonfeedback_view'),

    path('program/<int:program_id>/', views.program_detail, name='program_detail'),
    path('program/<int:program_id>/enroll/', views.enroll_in_program, name='enroll_in_program'),

    path('profile/edit/', views.common_edit_profile, name='common_edit_profile'),





]



