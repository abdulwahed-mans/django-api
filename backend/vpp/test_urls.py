# Path: backend/vpp/tests.py

from django.test import TestCase, Client
from django.urls import reverse

class MemberDashboardViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_member_dashboard_view(self):
        url = reverse('dashboard')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')
        # Add more assertions as needed