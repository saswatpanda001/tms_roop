from django.contrib.auth import get_user_model
from users.models import UserProfileModel
from main.models import FeedbackModel
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


        
@receiver(post_save, sender=FeedbackModel)
def create_feedback_username(sender, instance, created, **kwargs):
    print(sender, instance, created)

