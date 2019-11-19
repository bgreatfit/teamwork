from django.db import models
from accounts.models import User
# Create your models here.


class GIF(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='gifs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "gif"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "category"


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True)
    article = models.TextField(blank=True)
    category = models.ManyToManyField(Category, related_name='categories', blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.article}"

    class Meta:
        db_table = "article"


class ArticleComment(models.Model):
    comment = models.TextField(blank=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        db_table = "article_comment"


class GIFComment(models.Model):
    comment = models.TextField(blank=False)
    gif = models.ForeignKey(GIF, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        db_table = "gif_comment"


class Flag(models.Model):
    is_flagged = models.BooleanField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='flags')
    gif = models.ForeignKey(GIF, on_delete=models.CASCADE, related_name='flags')
    article_comment = models.ForeignKey(ArticleComment, on_delete=models.CASCADE, related_name='flags')
    gif_comment = models.ForeignKey(GIFComment, on_delete=models.CASCADE, related_name='flags')

    def __str__(self):
        return f"{self.is_flagged}"

    class Meta:
        db_table = "flag"
