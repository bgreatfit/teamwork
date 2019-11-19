from rest_framework import serializers
from .models import GIF, Article, Comment, Category


class GIFSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIF
        fields = ("image_url", "title")


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "comment", "article", "owner", "gif")
        extra_kwargs = {'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}

