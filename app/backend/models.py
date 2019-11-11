from django.db import models
from accounts.models import User
# Create your models here.


class GIF(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='gifs')
    created_at = models.DateTimeField(auto_now_add=True)


class Article(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)


