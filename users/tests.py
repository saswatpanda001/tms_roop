from django.test import TestCase, Client
from django.contrib.auth.models import User
from users.models import UserProfileModel
from django.urls import reverse

class UserManagementTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.employee_user = User.objects.create_user(username='employee', password='password123')
        self.manager_user = User.objects.create_user(username='manager', password='password123')
        self.hr_user = User.objects.create_user(username='hr', password='password123')
        
        UserProfileModel.objects.create(user=self.employee_user, role='employee')
        UserProfileModel.objects.create(user=self.manager_user, role='manager')
        UserProfileModel.objects.create(user=self.hr_user, role='HR')

    # 1. Test Employee Login Page Rendering
    def test_employee_login_page(self):
        response = self.client.get(reverse('users:employee_login'))
        self.assertEqual(response.status_code, 200)

    # 2. Test Manager Login Page Rendering
    def test_manager_login_page(self):
        response = self.client.get(reverse('users:manager_login'))
        self.assertEqual(response.status_code, 200)

    # 3. Test Management Login Page Rendering
    def test_management_login_page(self):
        response = self.client.get(reverse('users:management_login'))
        self.assertEqual(response.status_code, 200)

    # 4. Test Employee Dashboard Access
    def test_employee_dashboard_access(self):
        self.client.login(username='employee', password='password123')
        response = self.client.get(reverse('users:employee_dashboard'))
        self.assertEqual(response.status_code, 200)

    # 5. Test Manager Dashboard Access
    def test_manager_dashboard_access(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('users:manager_dashboard'))
        self.assertEqual(response.status_code, 200)

    # 6. Test Management Dashboard Access
    def test_management_dashboard_access(self):
        self.client.login(username='hr', password='password123')
        response = self.client.get(reverse('users:management_dashboard'))
        self.assertEqual(response.status_code, 200)

    # 7. Test Role-based Redirect for Employee
    def test_role_based_redirect_employee(self):
        self.client.login(username='employee', password='password123')
        response = self.client.get(reverse('users:role_redirect'))
        self.assertRedirects(response, reverse('users:employee_dashboard'))

    # 8. Test Role-based Redirect for Manager
    def test_role_based_redirect_manager(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('users:role_redirect'))
        self.assertRedirects(response, reverse('users:manager_dashboard'))

    # 9. Test Role-based Redirect for HR
    def test_role_based_redirect_hr(self):
        self.client.login(username='hr', password='password123')
        response = self.client.get(reverse('users:role_redirect'))
        self.assertRedirects(response, reverse('users:management_dashboard'))

    # 10. Test Role-based Redirect for Invalid Role
    def test_invalid_role_redirect(self):
        invalid_user = User.objects.create_user(username='invalid', password='password123')
        UserProfileModel.objects.create(user=invalid_user, role='unknown')
        self.client.login(username='invalid', password='password123')
        response = self.client.get(reverse('users:role_redirect'))
        self.assertRedirects(response, reverse('users:login_dashboard'))

    # 11. Test Access Without Profile Data
    def test_access_without_profile(self):
        new_user = User.objects.create_user(username='new_user', password='password123')
        self.client.login(username='new_user', password='password123')
        response = self.client.get(reverse('users:role_redirect'))
        self.assertRedirects(response, reverse('users:login'))

    # 12. Test Employee Dashboard Denied for Manager
    def test_employee_dashboard_denied_for_manager(self):
        self.client.login(username='manager', password='password123')
        response = self.client.get(reverse('users:employee_dashboard'))
        self.assertRedirects(response, reverse('users:employee_login'))

    # 13. Test Manager Dashboard Denied for HR
    def test_manager_dashboard_denied_for_hr(self):
        self.client.login(username='hr', password='password123')
        response = self.client.get(reverse('users:manager_dashboard'))
        self.assertRedirects(response, reverse('users:manager_login'))

    # 14. Test Management Dashboard Denied for Employee
    def test_management_dashboard_denied_for_employee(self):
        self.client.login(username='employee', password='password123')
        response = self.client.get(reverse('users:management_dashboard'))
        self.assertRedirects(response, reverse('users:management_login'))

    # 15. Test Login Dashboard Rendering
    def test_login_dashboard_page(self):
        response = self.client.get(reverse('users:login_dashboard'))
        self.assertEqual(response.status_code, 200)