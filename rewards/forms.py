from django import forms
from .models import RewardProgram

class RewardProgramForm(forms.ModelForm):
    class Meta:
        model = RewardProgram
        fields = ["title", "start_date", "end_date", "reward_type", "description", "invited_users"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter reward program title...",
            }),
            "start_date": forms.DateInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                "type": "date",
            }),
            "end_date": forms.DateInput(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                "type": "date",
            }),
            "reward_type": forms.TextInput(attrs={  # Since it's a CharField
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter reward type...",
            }),
            "description": forms.Textarea(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter description...",
                "rows": 4,
            }),
            "invited_users": forms.SelectMultiple(attrs={
                "class": "w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            }),
        }
