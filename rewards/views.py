from django.shortcuts import render, get_object_or_404, redirect
from .models import RewardProgram
from .forms import RewardProgramForm

def reward_list(request):
    programs = RewardProgram.objects.all()
    return render(request, 'reward_list.html', {'programs': programs})


def reward_detail(request, program_id):
    program = get_object_or_404(RewardProgram, id=program_id)
    return render(request, 'reward_detail.html', {'program': program})



def create_reward(request):
    if request.method == 'POST':
        form = RewardProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rewards:reward_list')
    else:
        form = RewardProgramForm()
    return render(request, 'reward_form.html', {'form': form})

def edit_reward(request, program_id):
    program = get_object_or_404(RewardProgram, id=program_id)
    if request.method == 'POST':
        form = RewardProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('rewards:reward_list')
    else:
        form = RewardProgramForm(instance=program)
    return render(request, 'reward_edit.html', {'form': form})
