from rest_framework import serializers
from .models import GIF, Article, GIFComment, ArticleComment, Category, Flag


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


class GIFCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIFComment
        fields = ("id", "comment","owner", "gif")
        extra_kwargs = {'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}


class FlagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flag
        fields = "__all__"

class ArticleCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArticleComment
        fields = ("id", "comment", "article", "owner")
        extra_kwargs = {'created_at': {'read_only': True}, 'updated_at': {'read_only': True}}

