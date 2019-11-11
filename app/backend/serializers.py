from rest_framework import serializers
from .models import GIF, Article


class GIFSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIF
        fields = ("image_url", "title")


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"

