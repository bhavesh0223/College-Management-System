from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from admin.models import AdminProfile

class AdminModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.admin = AdminProfile.objects.create(user=self.user, department='CS')

    def test_admin_profile_creation(self):
        self.assertEqual(self.admin.department, 'CS')
        self.assertEqual(str(self.admin), 'admin')

class AdminViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='admin123')
        self.admin = AdminProfile.objects.create(user=self.user, department='CS')

    def test_admin_login(self):
        response = self.client.post(reverse('admin:login'), {'username': 'admin', 'password': 'admin123'})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_admin_dashboard_access(self):
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('admin:dashboard'))
        self.assertEqual(response.status_code, 200)