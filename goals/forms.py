from django import forms
from .models import Goal, GoalComment

from django import forms
from .models import Goal, GoalComment

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["title", "description", "start_date", "end_date", "status"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"}
            ),
            "description": forms.Textarea(
                attrs={"class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500", "rows": 3}
            ),
            "start_date": forms.DateInput(
                attrs={"type": "date", "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"}
            ),
            "end_date": forms.DateInput(
                attrs={"type": "date", "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"}
            ),
            "status": forms.Select(
                attrs={"class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500"}
            ),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = GoalComment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "class": "w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500",
                    "rows": 3,
                    "placeholder": "Write your comment here...",
                }
            ),
        }
