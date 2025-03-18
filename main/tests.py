from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import *;
from users.models import *;

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

        # Create test user
        self.user = User.objects.create_user(username='testuser', password='password',email="abc@gmail.com")
        self.client.login(username='testuser', password='password')

        # Create a UserProfile for testuser
        self.user_profile = UserProfileModel.objects.create(user=self.user, avg_score=90)

        # Create test feedback
        FeedbackModel.objects.create(user=self.user, rating=4)

        # Create training program
        self.training_program = TrainingProgramModel.objects.create(name="Python Training")

        # Create an enrollment
        self.enrollment = EnrollmentModel.objects.create(user=self.user, program=self.training_program)

    def test_home_view(self):
        response = self.client.get(reverse('main:landing_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing.html')

    def test_dashboard_view(self):
        response = self.client.get(reverse('main:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_emp_profile_view(self):
        response = self.client.get(reverse('main:emp_profile', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_edit_profile_view(self):
        response = self.client.get(reverse('main:profile_edit', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_edit.html')

    def test_edit_profile_post(self):
        response = self.client.post(reverse('main:profile_edit', args=[self.user.id]), {
            'bio': 'Updated bio'
        })
        self.assertEqual(response.status_code, 302)  # Expect a redirect after saving

    def test_emp_details_view(self):
        response = self.client.get(reverse('main:emp_details', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emp_details.html')

    def test_emp_list_view(self):
        response = self.client.get(reverse('main:emp_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emp_list.html')

    def test_emp_edit_view(self):
        response = self.client.get(reverse('main:emp_edit', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'emp_edit.html')

    def test_emp_skillgap_view(self):
        response = self.client.get(reverse('main:emp_skillgap', args=[self.user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'skillgap.html')

    def test_training_programs_view(self):
        response = self.client.get(reverse('main:training_programs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'training.html')

    def test_program_detail_view(self):
        response = self.client.get(reverse('main:program_detail', args=[self.training_program.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'program_detail.html')

    def test_enroll_in_program_view(self):
        response = self.client.post(reverse('main:enroll_in_program', args=[self.training_program.id]))
        self.assertEqual(response.status_code, 302)  # Expect redirect after enrolling




from django.test import TestCase
from django.contrib.auth.models import User
from users.models import *;
from .models import *;

class ModelTests(TestCase):

    def setUp(self):
        """Create sample data for testing."""
        self.user = User.objects.create_user(username='testuser', password='password')
        self.skill = SkillModel.objects.create(name="Python")
        self.certification = CertificationModel.objects.create(name="AWS Certified")
        self.position = PositionModel.objects.create(title="Software Engineer")
        self.training = TrainingProgramModel.objects.create(name="Django Training", duration=30)
        self.job = JobModel.objects.create(title="Django Developer", description="Looking for Django expert", posted_by=self.user)
        self.application = JobApplicationModel.objects.create(job=self.job, applicant=self.user)
        self.user_profile = UserProfileModel.objects.create(user=self.user, role="employee")
        self.department = DepartmentModel.objects.create(name="IT Department")
        self.employee = EmployeeModel.objects.create(user_profile=self.user_profile, department=self.department)
        self.performance_review = PerformanceReviewModel.objects.create(employee=self.employee, score=4.5)

    def test_skill_model(self):
        """Test Skill model string representation."""
        self.assertEqual(str(self.skill), "Python")

  

    def test_position_model(self):
        """Test Position model string representation."""
        self.assertEqual(str(self.position), "Software Engineer")

    def test_training_program_model(self):
        """Test TrainingProgram model string representation."""
        self.assertEqual(str(self.training), "Django Training")

    def test_job_model(self):
        """Test Job model string representation."""
        self.assertEqual(str(self.job), "Django Developer")

    def test_job_application_model(self):
        """Test JobApplication model string representation."""
        self.assertEqual(str(self.application), f"{self.user.username} - {self.job.title}")

    def test_user_profile_model(self):
        """Test UserProfile model string representation."""
        self.assertEqual(str(self.user_profile), f"{self.user.username} - employee")

    def test_department_model(self):
        """Test Department model string representation."""
        self.assertEqual(str(self.department), "IT Department")

    def test_employee_model(self):
        """Test Employee model string representation."""
        self.assertEqual(str(self.employee), f"{self.user.username} - IT Department")

    def test_performance_review_model(self):
        """Test PerformanceReview model string representation."""
        self.assertEqual(str(self.performance_review), f"Review of {self.user.username} on None")
