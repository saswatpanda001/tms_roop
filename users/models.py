from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission


User = get_user_model()



class AchievementModel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    employee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)


    def __str__(self):
        return self.name

class SkillModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class CertificationModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class TrainingProgramModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class PositionModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class UserProfileModel(models.Model):
    EMPLOYEE = 'employee'
    MANAGER = 'manager'
    MANAGEMENT = 'management'
    ADMINISTRATOR = 'administrator'

    ROLE_CHOICES = [
        (EMPLOYEE, 'Employee'),
        (MANAGER, 'Manager'),
        (MANAGEMENT, 'Management'),
        (ADMINISTRATOR, 'Administrator'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=EMPLOYEE, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(SkillModel, blank=True, null=True)
    certifications = models.ManyToManyField(CertificationModel, blank=True, null=True)
    achievements = models.ManyToManyField(AchievementModel,blank=True, null=True)
    trainings = models.ManyToManyField(TrainingProgramModel, blank=True, null=True)
    rating = models.FloatField(default=0.0, blank=True, null=True)
    performance_history = models.TextField(blank=True, null=True)
    experience_years = models.IntegerField(default=0, blank=True, null=True)
    position = models.ForeignKey(PositionModel, on_delete=models.SET_NULL, null=True, blank=True)
    position_gen = models.CharField(max_length=100,null=True, blank=True)
    notifications_enabled = models.BooleanField(default=True, blank=True, null=True)
    joined = models.DateTimeField(default=timezone.now, blank=True, null=True)
    email = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(default="profile_pics/default_profile.png", upload_to="profile_pics", blank=True, null=True)


    def __str__(self):
        return f"{self.user.username} - {self.role}"




class DepartmentModel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    manager = models.ForeignKey('EmployeeModel', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class EmployeeModel(models.Model):
    user_profile = models.OneToOneField(UserProfileModel, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(DepartmentModel, on_delete=models.SET_NULL, null=True, blank=True)
    hire_date = models.DateField(default=timezone.now, blank=True, null=True)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.department.name if self.department else 'No Department'}"








class PerformanceReviewModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, blank=True, null=True)
    review_date = models.DateField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Review of {self.employee.user_profile.user.username} on {self.review_date}"


class SuccessionPlanModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE,blank=True, null=True)
    target_position = models.ForeignKey(PositionModel, on_delete=models.CASCADE,blank=True, null=True)
    preparedness_level = models.IntegerField(blank=True, null=True)
    estimated_ready_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Succession Plan for {self.employee.user_profile.user.username}"


class PromotionEligibilityModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE,blank=True, null=True)
    recommended_position = models.ForeignKey(PositionModel, on_delete=models.CASCADE,blank=True, null=True)
    recommendation_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return f"Promotion eligibility for {self.employee.user_profile.user.username}"


class ProjectModel(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.name

class EmployeeProjectModel(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE,blank=True, null=True)
    project = models.ForeignKey(ProjectModel, on_delete=models.CASCADE,blank=True, null=True)
    role_in_project = models.CharField(max_length=100,blank=True, null=True)
    contribution_level = models.CharField(max_length=100,blank=True, null=True)

    def __str__(self):
        return f"{self.employee.user_profile.user.username} in {self.project.name}"


class BlogModel(models.Model):
    author = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE,blank=True, null=True)
    title = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(default=timezone.now,blank=True, null=True)

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE,blank=True, null=True)
    commenter = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE,blank=True, null=True)
    comment_text = models.TextField(blank=True, null=True)
    comment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Comment by {self.commenter.user_profile.user.username}"



class NotificationModel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    notification_date = models.DateField(blank=True, null=True)
    is_read = models.BooleanField(default=False,blank=True, null=True)

    def __str__(self):
        return f"Notification for {self.recipient.username}"


