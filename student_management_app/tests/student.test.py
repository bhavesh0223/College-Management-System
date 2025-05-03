from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from student.models import StudentProfile

class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student', password='student123')
        self.student = StudentProfile.objects.create(user=self.user, roll_no='101')

    def test_student_profile_creation(self):
        self.assertEqual(self.student.roll_no, '101')
        self.assertEqual(str(self.student), 'student')

class StudentViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='student', password='student123')
        self.student = StudentProfile.objects.create(user=self.user, roll_no='101')

    def test_student_login(self):
        response = self.client.post(reverse('student:login'), {'username': 'student', 'password': 'student123'})
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_student_dashboard_access(self):
        self.client.login(username='student', password='student123')
        response = self.client.get(reverse('student:dashboard'))
        self.assertEqual(response.status_code, 200)