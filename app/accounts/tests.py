import json
from django.test import TestCase
# Add these imports at the top
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


# Create your tests here.
# Define this after the ModelTestCase
class EmployeeRegistrationAPIViewTestCase(APITestCase):
    """Test suite for the api views."""

    def test_invalid_password(self):
        """
        test that admin can create employee
        :param self:
        :return:
        """

        account_data = {
            "username": "Mike",
            "email": "mioshine@g.com",
            "password": "1234567",
            "confirm_password": "INVALID_PASSWORD"
        }
        response = self.client.post(
            reverse('accounts:create-user'),
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertTrue("error" in json.loads(response.content))

    def test_admin_can_create_a_employee(self):
        """
        test that admin can create employee
        :param self:
        :return:
        """

        account_data = {
            "username": "Mike",
            "email": "mioshine@g.com",
            "password": "1234567",
            "confirm_password": "1234567"
        }
        response = self.client.post(
            reverse('accounts:create-user'),
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("data" in json.loads(response.content))

    def test_employee_email_must_be_unique(self):
            """
            test that admin can create employee
            :param self:
            :return:
            """

            account_data = {
                "username": "Mike",
                "email": "mioshine@g.com",
                "password": "1234567",
                "confirm_password": "1234567"
            }
            response = self.client.post(
                reverse('accounts:create-user'),
                account_data,
                format="json")
            """Test the api has bucket creation capability."""
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

            account_data = {
                "username": "Mike",
                "email": "mioshine@g.com",
                "password": "1234567",
                "confirm_password": "1234567"
            }
            response = self.client.post(
                reverse('accounts:create-user'),
                account_data,
                format="json")
            """Test the api has bucket creation capability."""
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EmployeeLoginAPIViewTestCase(APITestCase):
    url = reverse("accounts:login")

    def setUp(self) -> None:
        self.email = "mojem@yahoo.com"
        self.password = "1234567"
        User.objects.create_user("mike", self.email, self.password)

    def test_authentication_without_password(self):
        """
            test that admin can create employee
            :param self:
            :return:
            """

        account_data = {
            "email": self.email,
            "password": ""
        }
        response = self.client.post(
            self.url,
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_with_invalid_password(self):
        """
            test that admin can create employee
            :param self:
            :return:
            """

        account_data = {
            "email": self.email,
            "password": "1234566"
        }
        response = self.client.post(
            self.url,
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_authentication_with_valid_data(self):
        """
            test that admin can create employee
            :param self:
            :return:
            """

        account_data = {
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(
            self.url,
            account_data,
            format="json")
        """Test the api has bucket creation capability."""
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("data" in json.loads(response.content))

