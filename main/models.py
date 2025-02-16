from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
from users.models import UserProfileModel




class FeedbackModel(models.Model):
    rating_choices = [
        ("1", "Poor"),
        ("2", "Fair"),
        ("3", "Good"),
        ("4", "Very Good"),
        ("5", "Excellent"),
    ]

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    profile = models.ForeignKey(UserProfileModel, blank=True, null=True, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=1, choices=rating_choices, blank=True, null=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.rating}"