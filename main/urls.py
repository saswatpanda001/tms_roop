
from django.urls import path
from main import views;

app_name = "main"

urlpatterns = [
    path('', views.home, name="landing_page"),
    path('dashboard', views.dashboard,name="dashboard"),
    path('emp/profile/<int:pk>', views.emp_profile, name="emp_profile"),
    path('emp/details/<int:pk>', views.emp_details, name="emp_details"),   
    path('emp/list', views.emp_list, name="emp_list"),
    path('emp/edit/<int:pk>', views.emp_edit, name="emp_edit"),
    path('emp/skillgap/<int:pk>', views.emp_skillgap, name="emp_skillgap"),
    path('emp/trainings/<int:pk>', views.emp_training, name="emp_training"),
    path('feedback', views.feedback, name="feedback"),

]



