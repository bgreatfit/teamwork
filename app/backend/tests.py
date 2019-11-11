from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from .models import GIF


class GIFCreateViewTestCase(APITestCase):
    url = reverse("gif-create")

    def setUp(self) -> None:
        self.username = "mike"
        self.email = "mike@y.com"
        self.password = "1234567"
        self.confirm_password = "1234567"
        user = User.objects.create_user(self.username, self.email, self.password)
        self.client.force_authenticate(user)

        # self.refresh = RefreshToken.for_user(user)
        #self.api_authentication()

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))

    def test_employee_can_create_gif(self):
        data = {"image": "http://url.com", "title": "aproko"}
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))        response = self.client.post(self.url, data)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

