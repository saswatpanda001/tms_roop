from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()





class FeedbackModel(models.Model):
    User = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True,null=True)
    username = models.CharField(default="not_specified",max_length=100, blank=True,null=True)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return str(self.username)[:10]

