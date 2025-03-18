from django.urls import path
from .views import create_goal, goal_list, goal_detail

app_name = "goals"

urlpatterns = [
    path("create/", create_goal, name="create_goal"),
    path("", goal_list, name="goal_list"),
    path("<int:pk>/", goal_detail, name="goal_detail"),
]