import json
from django.test import TestCase
# Add these imports at the top
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


# Create your tests here.
# Define this after the ModelTestCase
class AdminRegistrationAPIViewTestCase(APITestCase):
    """Test suite for the api views."""

    def test_admin_can_create_a_employee(self):
        """
        test that admin can create employee
        :param self:
        :return:
        """

        account_data = {"username": "Mike", "email": "mioshine@g.com",
                             "password": "1234567"}
        response = self.client.post(
            reverse('create-user'),
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.content)
        self.assertTrue("data" in json.loads(response.content))
