from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from users.models import UserProfileModel,SkillModel
User = get_user_model()



class FeedbackModel(models.Model):
    rating_choices = [
        ("1", "Poor"),
        ("2", "Fair"),
        ("3", "Good"),
        ("4", "Very Good"),
        ("5", "Excellent"),
    ]

    sender = models.ForeignKey(User, related_name="feedback_given", on_delete=models.CASCADE,blank=True, null=True)
    receiver = models.ForeignKey(User, related_name="feedback_received", on_delete=models.CASCADE,blank=True, null=True)
    description = models.TextField(blank=True, null=True,default="")
    category = models.CharField(max_length=200, blank=True, null=True)
    rating = models.CharField(max_length=1, choices=rating_choices, blank=True, null=True)
    performance_percentage = models.IntegerField(default=0,blank=True,null=True)  # Performance percentage (1-100)
    created_on = models.DateTimeField(default=timezone.now, blank=True, null=True)



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the feedback instance first

        if self.receiver:
            # Get the UserProfile of the receiver
            profile = UserProfileModel.objects.filter(user=self.receiver).first()
            if profile:
                # Calculate average rating
                feedbacks = FeedbackModel.objects.filter(receiver=self.receiver)
                total_ratings = feedbacks.count()
                if total_ratings > 0:
                    avg_rating = sum(int(fb.rating) for fb in feedbacks if fb.rating) / total_ratings
                else:
                    avg_rating = 0

                # Calculate average performance
                total_performance_scores = feedbacks.count()
                if total_performance_scores > 0:
                    avg_performance = sum(fb.performance_percentage for fb in feedbacks) / total_performance_scores
                else:
                    avg_performance = 0

                # Calculate avg_score based on custom logic
                total_skills = profile.skills.count()
                total_certifications = profile.certifications.count()
                total_trainings = profile.trainings.count()
                experience_years = profile.experience_years

                avg_score = (
                    (avg_rating * 20) + (avg_performance * 0.5) +
                    (total_skills * 10) + (total_certifications * 15) +
                    (total_trainings * 5) + (experience_years * 3)
                )

                # Update the user profile
                profile.avg_rating = round(avg_rating, 2)
                profile.avg_performance = round(avg_performance, 2)
                profile.avg_score = round(avg_score, 2)
                profile.save()

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.category} ({self.rating})"

    class Meta:
        ordering = ["-created_on"]  # Latest feedback first


class DomainSkillModel(models.Model):
    domain = models.CharField(max_length=100, unique=True)
    required_skills = models.ManyToManyField(SkillModel)

    def __str__(self):
        return self.domain


def skill_gap_analysis(user_profile):
    user_skills = user_profile.skills.all()  # Skills the user already has
    domain = user_profile.position_gen  # Assuming position_gen is the domain

    try:
        domain_skills = DomainSkillModel.objects.get(domain=domain).required_skills.all()
    except DomainSkillModel.DoesNotExist:
        return {"error": "No skill data for this domain."}

    # Find the missing skills
    missing_skills = domain_skills.exclude(id__in=user_skills.values_list('id', flat=True))


    recommended_trainings = TrainingProgram.objects.filter(skills__in=missing_skills).distinct()

    return {
        "user_skills": user_skills,
        "missing_skills": missing_skills,
        "recommended_trainings": recommended_trainings,
    }
