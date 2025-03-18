from django.urls import path
from .views import reward_list,reward_detail, edit_reward, create_reward

app_name = "rewards"

urlpatterns = [
    path('', reward_list, name='reward_list'),
    path('<int:program_id>/', reward_detail, name='reward_detail'),
    path('create/', create_reward, name='create_reward'),
    path('<int:program_id>/edit/', edit_reward, name='edit_reward'),



]