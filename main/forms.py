from django import forms
from users.models import BlogModel
from main.models import FeedbackModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'content']
    

class FeedbackForm(forms.ModelForm):
    rating_choices = [
        ("1", "Poor"),
        ("2", "Fair"),
        ("3", "Good"),
        ("4", "Very Good"),
        ("5", "Excellent"),
    ]

    rating = forms.ChoiceField(choices=rating_choices, widget=forms.RadioSelect)

    class Meta:
        model = FeedbackModel
        fields = ['category', 'feedback', 'rating']
