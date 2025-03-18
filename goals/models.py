from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    STATUS_CHOICES = [
        ("Draft", "Draft"),
        ("Submitted", "Submitted"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
    ]

    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goals")
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Draft")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.employee.username}"

class GoalComment(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.goal.title}"