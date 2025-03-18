
from django.contrib.auth import get_user_model
from users.models import UserProfileModel
from django.dispatch import receiver
from django.db.models.signals import post_save
User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(sender, instance, created)
    if created:
        a = UserProfileModel.objects.create(user=instance)
        print(a)
        a.save()
        print(a)


@receiver(post_save, sender=UserProfileModel)
def update_user_last_name(sender, instance, **kwargs):
    user = instance.user
    if user.last_name != instance.role:
        user.last_name = instance.role
        user.save()
 

