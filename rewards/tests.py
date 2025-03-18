from django.test import TestCase, Client
from django.urls import reverse
from .models import RewardProgram
from django.contrib.auth.models import User

class RewardProgramTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.reward = RewardProgram.objects.create(
            title='Test Reward',
            start_date='2024-01-01',
            end_date='2024-12-31',
            reward_type='Cashback',
            description='Test Description'
        )

    def test_reward_list_view(self):
        response = self.client.get(reverse('rewards:reward_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Reward')

    def test_reward_detail_view(self):
        response = self.client.get(reverse('rewards:reward_detail', args=[self.reward.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Description')

    def test_create_reward_view_get(self):
        response = self.client.get(reverse('rewards:create_reward'))
        self.assertEqual(response.status_code, 200)

    def test_create_reward_view_post(self):
        data = {
            'title': 'New Reward',
            'start_date': '2024-02-01',
            'end_date': '2024-12-31',
            'reward_type': 'Gift',
            'description': 'New Reward Description'
        }
        response = self.client.post(reverse('rewards:create_reward'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RewardProgram.objects.filter(title='New Reward').exists())

    def test_edit_reward_view_get(self):
        response = self.client.get(reverse('rewards:edit_reward', args=[self.reward.id]))
        self.assertEqual(response.status_code, 200)

    def test_edit_reward_view_post(self):
        data = {
            'title': 'Updated Reward',
            'start_date': '2024-01-01',
            'end_date': '2024-12-31',
            'reward_type': 'Cashback',
            'description': 'Updated Description'
        }
        response = self.client.post(reverse('rewards:edit_reward', args=[self.reward.id]), data)
        self.assertEqual(response.status_code, 302)
        self.reward.refresh_from_db()
        self.assertEqual(self.reward.title, 'Updated Reward')

    def test_invalid_reward_detail(self):
        response = self.client.get(reverse('rewards:reward_detail', args=[999]))
        self.assertEqual(response.status_code, 404)