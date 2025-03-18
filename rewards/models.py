from django.db import models
from django.contrib.auth.models import User

class RewardProgram(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    reward_type = models.CharField(max_length=100)
    description = models.TextField()
    invited_users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.title
