from django.db import models
from accounts.models import User
# Create your models here.


class GIF(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='gifs')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "gif"


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, )
    article = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.article}"

    class Meta:
        db_table = "article"


