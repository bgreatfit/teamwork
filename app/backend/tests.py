import json
from django.test import TestCase
# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import User
from .models import GIF, Article


class GIFCreateViewTestCase(APITestCase):
    url = reverse("gif-list")

    def setUp(self) -> None:
        self.username = "mike"
        self.email = "mike@y.com"
        self.password = "1234567"
        self.confirm_password = "1234567"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.client.force_authenticate(self.user)

        # self.refresh = RefreshToken.for_user(user)
        #self.api_authentication()

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))

    # def test_employee_can_create_gif(self):
    #     data = {"image": "http://url.com", "title": "aproko"}
    #     # self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))        response = self.client.post(self.url, data)
    #     response = self.client.post(self.url, data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_employee_can_get_all_gifs(self):
        data = {"image_url": "http://url.com", "title": "aproko"}
        GIF.objects.create(owner=self.user, **data)
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == GIF.objects.count())

    def test_employee_delete_gif(self):
        data = {"image_url": "http://url.com", "title": "aproko"}
        gif = GIF.objects.create(owner=self.user, **data)
        url = reverse('gif-detail', kwargs={'pk': gif.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ArticleListCreateViewTestCase(APITestCase):
    url = reverse("article-list")

    def setUp(self) -> None:
        self.username = "mike"
        self.email = "mike@y.com"
        self.password = "1234567"
        self.confirm_password = "1234567"
        user = User.objects.create_user(self.username, self.email, self.password)
        self.client.force_authenticate(user)

    def test_employee_can_create_article(self):
        data = {"title": "The king", "article": "this is a meaningful post"}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ArticleCreateViewTestCase(APITestCase):
    url = reverse("article-list")

    def setUp(self) -> None:
        self.username = "mike"
        self.email = "mike@y.com"
        self.password = "1234567"
        self.confirm_password = "1234567"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.client.force_authenticate(self.user)

        # self.refresh = RefreshToken.for_user(user)
        #self.api_authentication()

    # def api_authentication(self):
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))

    def test_employee_can_create_article(self):
        data = {"title": "The King", "article": "this awesome"}
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))
        # response = self.client.post(self.url, data)
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_employee_can_get_article(self):
        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))
        # response = self.client.post(self.url, data)
        data = {"title": "The king" , "article": "the people na dem"}
        article = Article.objects.create(owner=self.user, **data)
        response = self.client.get(self.url)
        self.assertTrue(len(json.loads(response.content)) == Article.objects.count())


class ArticleDetailViewTestCase(APITestCase):

    def setUp(self) -> None:
        self.username = "mike"
        self.email = "mike@y.com"
        self.password = "1234567"
        self.confirm_password = "1234567"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        data = {"article": "The purpose is to test this thing", "title":"the king"}
        self.article = Article.objects.create(owner=self.user, **data)
        self.url = reverse('article-detail', kwargs={"pk": self.article.pk})
        self.client.force_authenticate(self.user)

    def test_employee_authorised_to_update_article(self):
        user = User.objects.create_user('king', 'jeje@gmail.com', '5555555')
        self.client.force_authenticate(user)

        data = {"article": "this awesome"}

        # self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.refresh.access_token))
        # response = self.client.post(self.url, data)
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        response = self.client.patch(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_employee_can_update_article(self):
        data = {"title": "The King", "article": "this awesome"}
        response = self.client.put(self.url, data)
        article = Article.objects.get(id=self.article.id)

        self.assertEqual(json.loads(response.content).get('data')['article'], article.article)

    def test_employee_can_patch_article(self):
        data = {"article": "this linkin"}
        response = self.client.put(self.url, data)
        article = Article.objects.get(id=self.article.id)

        self.assertEqual(json.loads(response.content).get('data')['title'], article.title)

    def test_employee_can_delete_article(self):
        response = self.client.delete(self.url)
        self.assertEqual(204, response.status_code)

    def test_employee_delete_article_authorization(self):
        """
            Test to verify that put call with different user token
        """
        user = User.objects.create_user("newuser", "new@user.com", "newpass")
        self.client.force_authenticate(user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_employee_delete_article(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




