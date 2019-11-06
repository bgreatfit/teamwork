from django.test import TestCase
# Add these imports at the top
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

# Create your tests here.
# Define this after the ModelTestCase
class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.account_data = {'username': 'Mike', 'email': 'mioshine@g.com',
                                'password': '1234567'}
        self.response = self.client.post(
            reverse('create-user'),
            self.account_data,
            format="json")

    def test_admin_can_create_a_employee(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)