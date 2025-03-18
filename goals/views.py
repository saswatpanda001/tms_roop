

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Goal, GoalComment
from .forms import GoalForm, CommentForm

@login_required
def create_goal(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.employee = request.user
            goal.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm()
    return render(request, "goals/create_goal.html", {"form": form})

@login_required
def goal_list(request):
    goals = Goal.objects.filter(employee=request.user)
    goals_all = Goal.objects.all()
    return render(request, "goals/goal_list.html", {"goals": goals,"goals_all":goals_all})

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, id=pk)
    comments = goal.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.goal = goal
            comment.author = request.user
            comment.save()
            return redirect("goals:goal_detail", pk=goal.pk)
    else:
        form = CommentForm()
    
    return render(request, "goals/goal_detail.html", {"goal": goal, "comments": comments, "form": form})

