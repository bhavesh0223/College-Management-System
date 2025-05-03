from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from faculty.models import FacultyProfile

class FacultyModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='faculty', password='faculty123')
        self.faculty = FacultyProfile.objects.create(user=self.user, subject='Mathematics')

    def test_faculty_profile_creation(self):
        self.assertEqual(self.faculty.subject, 'Mathematics')
        self.assertEqual(str(self.faculty), 'faculty')

class FacultyViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='faculty', password='faculty123')
        self.faculty = FacultyProfile.objects.create(user=self.user, subject='Mathematics')

    def test_faculty_login(self):
        response = self.client.post(reverse('faculty:login'), {'username': 'faculty', 'password': 'faculty123'})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_faculty_dashboard_access(self):
        self.client.login(username='faculty', password='faculty123')
        response = self.client.get(reverse('faculty:dashboard'))
        self.assertEqual(response.status_code, 200)