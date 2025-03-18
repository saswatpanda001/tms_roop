from django.contrib import admin
from users.models import *

# Registering the models in the Django admin interface
admin.site.register(UserProfileModel)
admin.site.register(SkillModel)
admin.site.register(TrainingProgramModel)
admin.site.register(CertificationModel)
admin.site.register(PositionModel)
admin.site.register(DepartmentModel)
admin.site.register(EmployeeModel)
admin.site.register(PerformanceReviewModel)
admin.site.register(SuccessionPlanModel)
admin.site.register(PromotionEligibilityModel)
admin.site.register(ProjectModel)
admin.site.register(EmployeeProjectModel)
admin.site.register(BlogModel)
admin.site.register(CommentModel)
admin.site.register(NotificationModel)
admin.site.register(AchievementModel)
admin.site.register(SkillGapAnalysis)
admin.site.register(JobApplicationModel)
admin.site.register(JobModel)
admin.site.register(CommonFeedback)
admin.site.register(EnrollmentModel)

