from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Goal, GoalComment

class GoalTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.goal = Goal.objects.create(
            employee=self.user,
            title="Test Goal",
            description="Goal Description",
            start_date="2024-01-01",
            end_date="2024-12-31",
            status="Draft"
        )

    def test_goal_creation_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("goals:create_goal"))
        self.assertEqual(response.status_code, 200)

    def test_goal_submission(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("goals:create_goal"), {
            "title": "New Goal",
            "description": "New Goal Description",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "status": "Draft"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Goal.objects.filter(title="New Goal").exists())

    def test_goal_list_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("goals:goal_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.goal.title)

    def test_goal_detail_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("goals:goal_detail", args=[self.goal.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.goal.description)

    def test_goal_comment_submission(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("goals:goal_detail", args=[self.goal.id]), {"comment": "Great progress!"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(GoalComment.objects.filter(comment="Great progress!").exists())

    def test_unauthorized_goal_creation(self):
        response = self.client.get(reverse("goals:create_goal"))
        self.assertEqual(response.status_code, 302)

    def test_invalid_goal_access(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("goals:goal_detail", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_goal_status_choices(self):
        self.assertIn(self.goal.status, dict(Goal.STATUS_CHOICES))

    def test_comment_form_display(self):
        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("goals:goal_detail", args=[self.goal.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Add Comment")

    def test_unauthorized_comment_submission(self):
        response = self.client.post(reverse("goals:goal_detail", args=[self.goal.id]), {"comment": "Unauthorized comment"})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(GoalComment.objects.filter(comment="Unauthorized comment").exists())