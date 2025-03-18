from django import forms
from users.models import BlogModel
from main.models import FeedbackModel
from users.models import TrainingProgramModel, SkillModel, PositionModel, JobApplicationModel, JobModel, CommonFeedback, UserProfileModel


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = [
        'skills', 'skill_gap', 
            'certifications', 'achievements', 'trainings',
            'experience_years', 'position',
           'development_plans'
        ]
        widgets = {
            'skills': forms.CheckboxSelectMultiple(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
            'skill_gap': forms.CheckboxSelectMultiple(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
            'certifications': forms.CheckboxSelectMultiple(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
            'achievements': forms.CheckboxSelectMultiple(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
            'trainings': forms.CheckboxSelectMultiple(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
            'position': forms.Select(attrs={'class': 'block w-full px-4 py-2 border rounded-md focus:ring-2 focus:ring-blue-500'}),
          
           
        }

from django import forms
from .models import UserProfileModel

class CommonUserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        fields = ['phone_number', 'address', 'email', 'image']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your phone number'}),
            'address': forms.Textarea(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your address', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-2 border rounded-lg', 'placeholder': 'Enter your email'}),
            'image': forms.FileInput(attrs={'class': 'w-full p-2 border rounded-lg'}),
        }




class JobForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = ['title', 'description', 'position', 'required_skills', 'status']
        widgets = {
            'position': forms.CheckboxSelectMultiple(),
            'required_skills': forms.CheckboxSelectMultiple(),
        }

class JobApplicationForm(forms.ModelForm):
    resume = forms.FileField()
    
    class Meta:
        model = JobApplicationModel
        fields = ['resume']

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']
    
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = ["receiver", "category", "description", "rating", "performance_percentage"]
        widgets = {
            "receiver": forms.Select(attrs={"class": "w-full rounded-md border-gray-300 shadow-sm p-3 focus:border-blue-500 focus:ring-blue-500"}),
            "category": forms.TextInput(attrs={"class": "w-full rounded-md border-gray-300 shadow-sm p-3 focus:border-blue-500 focus:ring-blue-500", "placeholder": "Feedback Category"}),
            "description": forms.Textarea(attrs={"class": "w-full rounded-md border-gray-300 shadow-sm p-3 focus:border-blue-500 focus:ring-blue-500", "rows": 5, "placeholder": "Write your feedback here..."}),
            "rating": forms.Select(choices=FeedbackModel.rating_choices, attrs={"class": "w-full rounded-md border-gray-300 shadow-sm p-3 focus:border-blue-500 focus:ring-blue-500"}),
            "performance_percentage": forms.NumberInput(attrs={"class": "w-full rounded-md border-gray-300 shadow-sm p-3 focus:border-blue-500 focus:ring-blue-500", "min": 1, "max": 100, "placeholder": "Performance (1-100%)"}),
        }




class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgramModel
        fields = ['name', 'duration', 'skills', 'eligible_positions', 'level']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg focus:ring focus:ring-blue-300',
                'placeholder': 'Enter Training Program Name'
            }),
            'duration': forms.NumberInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg focus:ring focus:ring-blue-300',
                'placeholder': 'Duration in months'
            }),
            'skills': forms.SelectMultiple(attrs={
                'class': 'form-multiselect w-full p-2 border rounded-lg focus:ring focus:ring-blue-300'
            }),
            'eligible_positions': forms.SelectMultiple(attrs={
                'class': 'form-multiselect w-full p-2 border rounded-lg focus:ring focus:ring-blue-300'
            }),
            'level': forms.TextInput(attrs={
                'class': 'form-input w-full p-2 border rounded-lg focus:ring focus:ring-blue-300',
                'placeholder': 'Training Program Level'
            }),
        }


class CommonFeedbackForm(forms.ModelForm):
    class Meta:
        model = CommonFeedback
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'placeholder': 'Enter title'}),
            'description': forms.Textarea(attrs={'class': 'w-full p-2 border border-gray-300 rounded-md', 'rows': 4, 'placeholder': 'Write your feedback...'}),
        }