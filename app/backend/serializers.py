from rest_framework import serializers
from .models import GIF


class GIFSerializer(serializers.ModelSerializer):

    class Meta:
        model = GIF
        fields = ("image_url", "title")

